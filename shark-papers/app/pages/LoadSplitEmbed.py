import streamlit as st
from src.embedding.huggingface_embedding import add_embedding
from src.embedding.openai_embedding import add_embedding_openai
from src.loader.loader import load_pdf
from src.transformer.splitter import split_documents

nb_openai_used_tokens = 0


@st.cache_data
def load_file(strbytepath):
    return load_pdf(strbytepath)


def init_session_state(objs: list):
    for obj in objs:
        if obj not in st.session_state:
            st.session_state[obj] = None


def gst(obj: str):
    return st.session_state[obj]


init_session_state(["doc"])

st.title("Q&A Pipeline: Load, Transform, Embed, Similarity, Generation")

st.subheader("Load your content")

uploaded_file = st.file_uploader("Load any pdf file", type=["pdf"])
if uploaded_file is not None:
    doc = gst("doc")
    doc = load_file(uploaded_file)
    st.warning(f"There are {len(doc.sub_documents)} pages")

    with st.form("Choose your splitters?"):
        splitters = st.multiselect(
            "Pick your splitters", ["Page", "Recursive"], default="Recursive"
        )
        split_button = st.form_submit_button("Launch Splitter")
    if "Recursive" in splitters:
        doc = split_documents([doc])[0]
        st.warning(
            f"Split is done, there are now {len(doc.sub_documents)} sub_documents"
        )

    with st.form("Choose your embeddings"):
        embeddings = st.multiselect(
            "Pick your embeddings", ["OpenAI", "HuggingFace"], default=None
        )
        embed_button = st.form_submit_button("Launch Embeddings")

    if embed_button:
        if "OpenAI" in embeddings:
            doc_ai, nb_openai_used_tokens = add_embedding_openai(
                doc, nb_openai_used_tokens
            )

        if "HuggingFace" in embeddings:
            doc_hug = add_embedding(doc)