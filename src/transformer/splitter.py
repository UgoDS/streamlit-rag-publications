from langchain_text_splitters import (
    CharacterTextSplitter,
    TokenTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from data_model.loader import Splitter


def split_text(text, splitter, chunk_size=500, chunk_overlap=20):
    if splitter == Splitter.CHARACTERTEXT.value:
        text_splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )
    elif splitter == Splitter.RECURSIVECHARACTERTEXT.value:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )
    elif splitter == Splitter.SEMANTICCHUNKER.value:
        text_splitter = SemanticChunker(OpenAIEmbeddings())
    elif splitter == Splitter.TOKENTEXTPLITTER.value:
        text_splitter = TokenTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
    else:
        raise ValueError
    texts = text_splitter.create_documents([text])
    return texts
