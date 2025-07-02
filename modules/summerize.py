from pipelines import Summarization
from utils.file_handlers import extract_text
import streamlit as st

def show_summerization():
    st.subheader("Text Summarization")
    uploaded_file = st.file_uploader("Upload a document to summarize", type=["txt", "pdf", "docx"])
    input_text = st.text_area("Or enter text to summarize", height=200)
    if uploaded_file:
        input_text = extract_text(uploaded_file)
    if input_text:
        if st.button("Summarize"):
            with st.spinner("Generating summary..."):
                summary = Summarization(input_text).predict()
                st.subheader("Summary")
                st.write(summary[0]['summary_text'])
                st.write(f"Original length: {len(input_text)} characters")
                st.write(f"Summary length: {len(summary[0]['summary_text'])} characters")