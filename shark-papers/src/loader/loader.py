from pypdf import PdfReader
import uuid
from src.data_model.document import Document, SubDocument


def load_pdf(pdf_path: str):
    reader = PdfReader(pdf_path)
    nb_pages = len(reader.pages)
    list_sub_docs = []
    for page in reader.pages:
        list_sub_docs.append(SubDocument(sub_id=uuid.uuid1(), text=page.extract_text()))
    return Document(id=uuid.uuid1(), nb_pages=nb_pages, sub_documents=list_sub_docs)
