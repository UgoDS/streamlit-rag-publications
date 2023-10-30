import pickle
from datetime import date
from time import sleep

import openai
import tqdm
from src.data_model.document import Document
from src.utils.openai_utils import get_openai_key

openai.api_key = get_openai_key()
OPENAI_MODEL_EMBEDDING = "text-embedding-ada-002"


def add_embedding_openai(doc: Document, nb_openai_used_tokens: int):
    doc_ai = doc.model_copy(deep=True)
    doc_ai.embedding_model = OPENAI_MODEL_EMBEDDING
    for idx_sub_doc in tqdm(range(0, len(doc_ai.sub_documents), 20)):
        results = get_embedding(
            [
                doc_.text
                for doc_ in doc_ai.sub_documents[idx_sub_doc : idx_sub_doc + 20]
            ],
            model=OPENAI_MODEL_EMBEDDING,
        )
        for idx, emb in enumerate(results["data"]):
            doc_ai.sub_documents[idx_sub_doc + idx].embedding = emb["embedding"]
        nb_openai_used_tokens += get_nb_tokens(results)
        sleep(20)
    save_embeddings(doc_ai)
    return doc_ai, nb_openai_used_tokens


def get_embedding(list_text, model=OPENAI_MODEL_EMBEDDING):
    list_text = [text.replace("\n", " ") for text in list_text]
    return openai.Embedding.create(input=list_text, model=model)


def get_embedding_values(embedding: dict):
    return embedding["data"]


def get_nb_tokens(embedding: dict):
    return embedding["usage"]["total_tokens"]


def save_embeddings(embeddings):
    str_date = date.today().strftime("%Y%m%d")
    with open(
        f"../data/processed/province-sud/BaieDesCitrons_barriere_01062023_{str_date}.pickle",
        "wb",
    ) as handle:
        pickle.dump(embeddings, handle, protocol=pickle.HIGHEST_PROTOCOL)
