from enum import Enum
from dataclasses import dataclass


class Loader(Enum):
    PYPDF = "PyPDF"
    PYPDFIUM = "pypdfium"
    PYMUPDF = "PyMuPDF"
    PDFPLUMBER = "pdfplumber"


@dataclass
class LoaderDescription:
    name: str
    url: str
    description: str
    github_stars: int
