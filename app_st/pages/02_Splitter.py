import streamlit as st
from app_st.utils.utils_loader import display_loader_description
from app_st.utils.utils_st import init_session_states, gst, load_file, split_file, get_nb_pages
from data_model.loader import Loader, Splitter

CONFIG_SPLITTER_PATH = "configs/splitter_config.yml"
st.set_page_config("Splitter", layout="wide", initial_sidebar_state="collapsed")
st.sidebar.title("Parameters")
chunk_size = int(st.sidebar.text_input("Chunk Size", 200))
chunk_overlap = int(st.sidebar.text_input("Chunk Overlap", 20))

init_session_states(["dict_docs", "splitter_selected", "page_selected"])
splitter_selected = gst("splitter_selected")
dict_docs = gst("dict_docs")
if "nb_pages" not in st.session_state:
    st.session_state["nb_pages"] = 1
nb_pages = gst("nb_pages")

st.title("Splitter Visualizer")
st.subheader("Rational")
st.write("The splitter might have a great influence on the rest of the pipeline.")

st.subheader("Upload a document")
uploaded_file = st.file_uploader("Load any pdf file", type=["pdf"])
if uploaded_file is not None:
    loader_selected = st.selectbox(
        "Pick a loader", [pdf_loader.value for pdf_loader in Loader], 2
    )
    nb_pages = get_nb_pages(uploaded_file)
    st.info(f"There are {nb_pages} pages")
    with st.expander("Compare Splitters"):
        st.subheader("Visualize the difference between splitters")
        display_loader_description(CONFIG_SPLITTER_PATH)
        with st.form("Select splitters"):
            splitter_selected = st.multiselect(
                "Choose splitters", [pdf_loader.value for pdf_loader in Splitter], None
            )
            button_loaders = st.form_submit_button("Launch loading")
        if button_loaders:
            pass

        if len(splitter_selected) > 0:
            page_selected = st.selectbox(
                "Which page?", [page_num for page_num in range(0, nb_pages)], 0
            )
            cols = st.columns(len(splitter_selected))
            dict_docs = {}
            file_loaded = load_file(uploaded_file, loader_selected)
            for idx, col in enumerate(cols):
                splitter_ = splitter_selected[idx]
                col.subheader(splitter_)
                dict_docs[f"doc_{splitter_}"] = split_file(
                    file_loaded.sub_documents[page_selected].text, splitter_, chunk_size, chunk_overlap
                )
                col.write(
                    [x.page_content for x in dict_docs[f"doc_{splitter_}"]]
                )
