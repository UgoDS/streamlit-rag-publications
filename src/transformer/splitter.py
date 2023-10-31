import re
import uuid
from typing import Iterable, List

from data_model.document import Document, SubDocument

DEFAULT_SEPARATORS = ["\n\n", "\n", " ", ""]


def split_documents(docs: List[Document]) -> List[Document]:
    new_docs = []
    for doc in docs:
        new_sub_documents = []
        for sub_doc in doc.sub_documents:
            list_txt = recursive_text_split(
                text=sub_doc.text,
                separators=DEFAULT_SEPARATORS,
                keep_separator=False,
                chunk_size=500,
                chunk_overlap=50,
            )
            for text in list_txt:
                new_sub_documents.append(SubDocument(sub_id=uuid.uuid1(), text=text))
        doc.sub_documents = new_sub_documents
        doc.nb_sub_docs = len(new_sub_documents)
        doc.splitter_method = "Recursive"
        new_docs.append(doc)
    return new_docs


def recursive_text_split(
    text: str,
    separators: List[str],
    keep_separator: bool = False,
    chunk_size: int = 4000,
    chunk_overlap: int = 200,
) -> List[str]:
    """Split incoming text and return chunks."""
    final_chunks = []
    # Get appropriate separator to use
    separator, new_separators = remove_not_found_separator(text, separators)
    splits = _split_text_with_regex(text, separator, keep_separator)

    # Now go merging things, recursively splitting longer texts.
    _good_splits = []
    _separator = "" if keep_separator else separator
    for s in splits:
        if len(s) < chunk_size:
            _good_splits.append(s)
        else:
            if _good_splits:
                merged_text = _merge_splits(
                    _good_splits, _separator, chunk_size, chunk_overlap
                )
                final_chunks.extend(merged_text)
                _good_splits = []
            if not new_separators:
                final_chunks.append(s)
            else:
                other_info = recursive_text_split(
                    s, new_separators, chunk_size, chunk_overlap
                )
                final_chunks.extend(other_info)
    if _good_splits:
        merged_text = _merge_splits(_good_splits, _separator, chunk_size, chunk_overlap)
        final_chunks.extend(merged_text)
    return final_chunks


def remove_not_found_separator(text: str, separators: List[str] = DEFAULT_SEPARATORS):
    # Get appropriate separator to use
    separator = separators[-1]
    new_separators = []
    for i, _s in enumerate(separators):
        _separator = re.escape(_s)
        if _s == "":
            separator = _s
            break
        if re.search(_separator, text):
            separator = _s
            new_separators = separators[i + 1 :]
            break
    return separator, new_separators


def _merge_splits(
    splits: Iterable[str], separator: str, chunk_size: int, chunk_overlap: int
) -> List[str]:
    # We now want to combine these smaller pieces into medium size
    # chunks to send to the LLM.
    separator_len = len(separator)

    docs = []
    current_doc = []
    total = 0
    for d in splits:
        _len = len(d)
        if total + _len + (separator_len if len(current_doc) > 0 else 0) > chunk_size:
            if len(current_doc) > 0:
                doc = separator.join(current_doc)
                if doc is not None:
                    docs.append(doc)
                # Keep on popping if:
                # - we have a larger chunk than in the chunk overlap
                # - or if we still have any chunks and the length is long
                while total > chunk_overlap or (
                    total + _len + (separator_len if len(current_doc) > 0 else 0)
                    > chunk_size
                    and total > 0
                ):
                    total -= len(current_doc[0]) + (
                        separator_len if len(current_doc) > 1 else 0
                    )
                    current_doc = current_doc[1:]
        current_doc.append(d)
        total += _len + (separator_len if len(current_doc) > 1 else 0)
    doc = separator.join(current_doc)
    if doc is not None:
        docs.append(doc)
    return docs


def _split_text_with_regex(
    text: str, separator: str, keep_separator: bool
) -> List[str]:
    _separator = re.escape(separator)
    # Now that we have the separator, split the text
    if separator:
        if keep_separator:
            # The parentheses in the pattern keep the delimiters in the result.
            _splits = re.split(f"({_separator})", text)
            splits = [_splits[i] + _splits[i + 1] for i in range(1, len(_splits), 2)]
            if len(_splits) % 2 == 0:
                splits += _splits[-1:]
            splits = [_splits[0]] + splits
        else:
            splits = re.split(_separator, text)
    else:
        splits = list(text)
    return [s for s in splits if s != ""]
