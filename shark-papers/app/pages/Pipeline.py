import streamlit as st
from src.embedding.huggingface_embedding import add_embedding
from src.embedding.openai_embedding import add_embedding_openai
from src.loader.loader import load_pdf
from src.transformer.splitter import split_documents

nb_openai_used_tokens = 0


@st.cache
def load_file(strbytepath):
    return load_pdf(strbytepath)


st.title("Q&A Pipeline: Load, Transform, Embed, Similarity, Generation")

st.subheader("Load your content")

uploaded_file = st.file_uploader("Load any pdf file", type=["pdf"])
if uploaded_file is not None:
    doc = load_file(uploaded_file)
    st.warning(f"There are {len(doc.sub_documents)} pages")

    with st.form("Split the document?"):
        split_button = st.form_submit_button("Do you want to split it?")
    if split_button:
        docs = split_documents([doc])

    with st.form("Choose your embeddings"):
        embeddings = st.multiselect(
            "Pick your embeddings", ["OpenAI", "HuggingFace"], default=None
        )

        if "OpenAI" in embeddings:
            doc_ai, nb_openai_used_tokens = add_embedding_openai(
                docs[0], nb_openai_used_tokens
            )

        if "HuggingFace" in embeddings:
            doc_hug = add_embedding(docs[0])
