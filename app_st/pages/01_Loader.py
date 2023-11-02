import streamlit as st
from app_st.utils.utils_loader import display_loader_description
from app_st.utils.utils_st import init_session_states, gst, load_file
from data_model.loader import Loader
from data_model.state import State
from app_st.utils.utils_file import save_pickle, create_file_name

CONFIG_LOADER_PATH = "configs/loader_config.yml"
st.set_page_config("Loader", layout="wide", initial_sidebar_state="collapsed")

init_session_states(["dict_docs", "loader_selected", "page_selected"])
loader_selected = gst("loader_selected")
dict_docs = gst("dict_docs")
if "nb_pages" not in st.session_state:
    st.session_state["nb_pages"] = 1
nb_pages = gst("nb_pages")

st.title("Loader Visualizer")
st.subheader("Rational")
st.write("The loader might have a great influence on the rest of the pipeline.")
st.write(
    "For example, I have been facing extra space, like 'visual ization' instead of 'visualization', which change word meaning."
)

st.subheader("Upload a document")
uploaded_file = st.file_uploader("Load any pdf file", type=["pdf"])
if uploaded_file is not None:
    with st.expander("Compare Loaders"):
        st.subheader("Visualize the difference between loaders")
        display_loader_description(CONFIG_LOADER_PATH)
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
        with st.form("Save Loaded data"):
            picked_loader = st.selectbox(
                "Choose one", [pdf_loader.value for pdf_loader in Loader], None
            )
            button_save = st.form_submit_button("Save")
        if button_save:
            file_path = create_file_name(
                uploaded_file.name, State.LOADER.value, picked_loader
            )
            save_pickle(dict_docs[f"doc_{picked_loader}"], file_path)
            st.warning(f"Save here: {file_path}")
