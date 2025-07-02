from pipelines import Translation
from utils.file_handlers import extract_text
import streamlit as st

def show_translation():
    st.subheader("French to English Translation")
    uploaded_file = st.file_uploader("Upload French text", type=["txt", "pdf", "docx"])
    french_text = st.text_area("Or enter French text to translate", height=200)
    if uploaded_file:
        french_text = extract_text(uploaded_file)
    if french_text:
        if st.button("Translate"):
            with st.spinner("Translating..."):
                translation = Translation(french_text).predict()
                st.subheader("English Translation")
                st.write(translation[0]['translation_text'])
                st.write(f"Original French: {french_text[:200]}...")