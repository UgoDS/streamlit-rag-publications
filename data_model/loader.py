from enum import Enum
from dataclasses import dataclass
from typing import Optional


class Loader(Enum):
    PYPDF = "PyPDF"
    PYPDFIUM = "pypdfium"
    PYMUPDF = "PyMuPDF"
    PDFPLUMBER = "pdfplumber"


class Splitter(Enum):
    CHARACTERTEXT = "CharacterTextSplitter"
    RECURSIVECHARACTERTEXT = "RecursiveCharacterTextSplitter"
    SEMANTICCHUNKER = "SemanticChunker"
    TOKENTEXTPLITTER = "TokenTextSplitter"


@dataclass
class LoaderDescription:
    name: str
    url: str
    description: str
    github_stars: Optional[int]
