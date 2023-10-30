import uuid

from pydantic import BaseModel


class SubDocument(BaseModel):
    sub_id: uuid.UUID = None
    text: str = None
    embedding: list[float] = None


class Document(BaseModel):
    id: uuid.UUID = None
    author: str = None
    nb_pages: int = None
    nb_sub_docs: int = None
    sub_documents: list[SubDocument] = None
    embedding_model: str = None
    splitter_method: str = None
