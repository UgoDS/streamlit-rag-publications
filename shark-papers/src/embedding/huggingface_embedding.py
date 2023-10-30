from tqdm import tqdm
from sentence_transformers import SentenceTransformer, util
from src.data_model.document import Document

ST_MODEL_EMBEDDING = "multi-qa-MiniLM-L6-cos-v1"

model = SentenceTransformer(ST_MODEL_EMBEDDING)


def add_embedding(doc: Document):
    doc_st = doc.model_copy(deep=True)
    doc_st.embedding_model = ST_MODEL_EMBEDDING

    for sub_docs in tqdm(doc_st.sub_documents):
        txt_ = sub_docs.text.replace("\n", " ")
        sub_docs.embedding = list(model.encode(txt_))
    return doc_st
