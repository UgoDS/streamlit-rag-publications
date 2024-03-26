import streamlit as st
import base64
from src.loader.loader import load_pdf
from src.transformer.splitter import split_text


def get_nb_pages(uploaded_file):
    loader_ = "PyPDF"
    return load_file(uploaded_file, loader_).nb_pages


def split_file(text, splitter, *args):
    return split_text(text, splitter, *args)


@st.cache_data
def load_file(strbytepath, loader):
    return load_pdf(strbytepath, loader)


def init_session_states(objs: list):
    for obj in objs:
        if obj not in st.session_state:
            st.session_state[obj] = None


def gst(obj: str):
    return st.session_state[obj]


def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    # Embedding PDF in HTML
    pdf_display = f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 100%;">"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
