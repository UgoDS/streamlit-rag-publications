import streamlit as st
import base64
import urllib.request
from src.loader.loader import load_pdf


@st.cache_data
def load_file(strbytepath):
    return load_pdf(strbytepath)


def init_session_state(objs: list):
    for obj in objs:
        if obj not in st.session_state:
            st.session_state[obj] = None


def gst(obj: str):
    return st.session_state[obj]


def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 100%;">"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
