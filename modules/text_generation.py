from pipelines import TextGenerator
from utils.file_handlers import extract_text
import streamlit as st

def show_text_generation():
    st.subheader("Text Generation")
    prompt = st.text_area("Enter a prompt to continue", height=100)
    length = st.slider("Max length", 50, 500, 100)
    if prompt:
        if st.button("Generate Text"):
            with st.spinner("Generating text..."):
                generator = TextGenerator(prompt,length)
                generated = generator.predict()[0]
                st.subheader("Generated Text")
                st.write(generated['generated_text'])
                word_count = len(generated['generated_text'].split())
                st.success(f"Word count: {word_count} words")
                