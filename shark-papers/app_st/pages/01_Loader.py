import streamlit as st
from app_st.utils_st import displayPDF, init_session_state, gst, load_file

init_session_state(["doc"])

st.title("Loader Visualizer")

st.subheader("Load a document")

uploaded_file = st.file_uploader("Load any pdf file", type=["pdf"])
if uploaded_file is not None:

    with st.form("Select a loader"):
        loader_selecter = st.selectbox("Choose one", ["PyPDF"])
        page_selected = st.selectbox(
            "Choose a page", [pag_num for pag_num in range(0, doc.nb_pages)]
        )
        button_loader = st.form_submit_button("Load")

    if button_loader:
        doc = gst("doc")
        doc = load_file(uploaded_file)
        st.warning(f"There are {len(doc.sub_documents)} pages")
        # displayPDF(
        #    "/Users/ugo/Documents/shark_attack/shark-papers/data/raw/province-sud/BaieDesCitrons_barriere_01062023.pdf"
        # )
        st.write(doc.sub_documents[page_selected].text)
