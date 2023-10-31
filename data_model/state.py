from enum import Enum


class State(Enum):
    LOADER = "interim/loader"
    SPLITTER = "interim/splitter"
    TRANSFORMER = "interim/transformer"
    EMBEDDER = "processed/embedder"
