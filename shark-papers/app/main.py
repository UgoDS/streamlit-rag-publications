import pandas as pd
import streamlit as st

st.header(":shark: Shark Papers")
st.divider()
st.subheader("Project description")
st.write("Question Answering on Shark publications in New Caledonia")
st.write(
    "You should be able to upload any publication, ask a question and find the relevant part of documents, and finally generate a final answer given the contents found."
)

df_results = pd.DataFrame(
    columns=["Name", "Year", "Author", "Description", "IsIndexed", "NbPages"]
)
df_results.loc[0, :] = [
    "Barrière Baie des Citrons",
    2023,
    "Province Sud",
    "Etude d’impact de la mise en place d’un dispositif de barrière anti-requin au niveau de la Baie des Citrons",
    True,
    20,
]
st.table(df_results)
