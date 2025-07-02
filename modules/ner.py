from pipelines import NER
from utils.file_handlers import extract_text
import streamlit as st
import pandas as pd 

def show_NER():
    st.subheader("Named Entity Recognition (NER) Tool")
    uploaded_file = st.file_uploader("Upload file", type=["txt", "pdf", "docx", "csv"])
    if uploaded_file:
        text = extract_text(uploaded_file)
        with st.expander("View Extracted Text"):
            st.text(text[:5000] + "...") 
        entities = NER(text).predict()
        entity_groups = {}
        for entity in entities:
            group = entity['entity_group']
            if group not in entity_groups:
                entity_groups[group] = []
            entity_groups[group].append(entity['word'])
        st.header("Named Entities Found")
        for group, words in entity_groups.items():
            with st.expander(f"{group} ({len(words)} found)"):
                st.table(pd.DataFrame({
                    "Entity": words,
                    "Type": group
                }))