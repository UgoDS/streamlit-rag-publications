import numpy as np
from sentence_transformers import util
from src.data_model.document import Document


def find_top_sub_documents(doc: Document, query_embedding: list, top_n: int = 5):
    passage_embedding = [doc_.embedding for doc_ in doc.sub_documents]
    similarities = util.dot_score(query_embedding, passage_embedding)
    top_indices = np.argsort(similarities)[0][-top_n:]
    list_context = []
    for ind in top_indices:
        print(similarities[0][ind])
        list_context.append(doc.sub_documents[ind].text)
    list_context
