import streamlit as st
from app_st.utils_st import init_session_states, gst, load_file
from data_model.loader import Loader

st.set_page_config("Loader", layout="wide")

init_session_states(["dict_docs", "loader_selected", "page_selected"])
loader_selected = gst("loader_selected")
dict_docs = gst("dict_docs")
if "nb_pages" not in st.session_state:
    st.session_state["nb_pages"] = 1
nb_pages = gst("nb_pages")


st.title("Loader Visualizer")

st.subheader("Upload a document")

uploaded_file = st.file_uploader("Load any pdf file", type=["pdf"])
if uploaded_file is not None:
    with st.expander("Compare Loaders"):
        st.subheader("Visualize the difference between loaders")
        with st.form("Select loaders"):
            loader_selected = st.multiselect(
                "Choose loaders", [pdf_loader.value for pdf_loader in Loader], None
            )
            button_loaders = st.form_submit_button("Launch loading")
        if button_loaders:
            pass

        def get_nb_pages():
            loader_ = "PyPDF"
            return load_file(uploaded_file, loader_).nb_pages
        
        nb_pages = get_nb_pages() 
        st.warning(f"There are {nb_pages} pages")

        if len(loader_selected) > 0:
            page_selected = st.selectbox(
                "Which page?", [page_num for page_num in range(0, nb_pages)], 0
            )
            cols = st.columns(len(loader_selected))
            dict_docs = {}
            for idx, col in enumerate(cols):
                loader_ = loader_selected[idx]
                col.subheader(loader_)
                dict_docs[f"doc_{loader_}"] = load_file(uploaded_file, loader_)
                col.write(dict_docs[f"doc_{loader_}"].sub_documents[page_selected].text)
    with st.expander("Pick a loader"):
        picked_loader = st.selectbox(
            "Choose one", [pdf_loader.value for pdf_loader in Loader], None
        )
        if picked_loader:
            pass
