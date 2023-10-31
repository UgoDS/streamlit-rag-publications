from enum import Enum


class Loader(Enum):
    PYPDF = "PyPDF"
    PYPDFIUM = "pypdfium"
    PYMUPDF = "PyMuPDF"
    PDFPLUMBER = "pdfplumber"
