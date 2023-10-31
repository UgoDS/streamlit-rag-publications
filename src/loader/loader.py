import uuid

from pypdf import PdfReader
import pypdfium2 as pdfium
import fitz
import pdfplumber
from data_model.document import Document, SubDocument
from data_model.loader import Loader


def load_pdf(pdf_path: str, loader: str):
    nb_pages, list_txt_pages = extract_text(pdf_path, loader)
    list_sub_docs = []
    for page in list_txt_pages:
        list_sub_docs.append(SubDocument(sub_id=uuid.uuid1(), text=page))
    return Document(id=uuid.uuid1(), nb_pages=nb_pages, sub_documents=list_sub_docs)


# TODO add parameters for each loader
def extract_text(pdf_path, loader):
    if loader == Loader.PYPDF.value:
        reader = PdfReader(pdf_path)
        nb_pages = len(reader.pages)
        list_txt_pages = [page.extract_text() for page in reader.pages]
    elif loader == Loader.PYPDFIUM.value:
        pdf = pdfium.PdfDocument(pdf_path)
        nb_pages = len(pdf)
        list_txt_pages = [page.get_textpage().get_text_range() for page in pdf]
    elif loader == Loader.PYMUPDF.value:
        pdf = fitz.open(stream=pdf_path.read(), filetype="pdf")
        nb_pages = len(pdf)
        list_txt_pages = [page.get_text().encode("utf8") for page in pdf]
    elif loader == Loader.PDFPLUMBER.value:
        pdf = pdfplumber.open(pdf_path)
        nb_pages = len(pdf.pages)
        list_txt_pages = [page.extract_text() for page in pdf.pages]
    else:
        raise ValueError
    return nb_pages, list_txt_pages
