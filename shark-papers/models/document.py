from pydantic import BaseModel
import uuid


class SubDocument(BaseModel):
    sub_id: uuid.UUID = None
    text: str = None


class Document(BaseModel):
    id: uuid.UUID = None
    author: str = None
    nb_pages: int = None
    sub_documents: list[SubDocument] = None