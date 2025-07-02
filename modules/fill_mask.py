from pipelines import FillMask
from utils.file_handlers import extract_text
import streamlit as st

def show_fill_mask():
    st.subheader("Fill in the Blank")
    user_input = st.text_input("Enter a sentence with a blank (use ___ for the blank)")
    if user_input:
        if '___' not in user_input:
            st.warning("Please include a blank using three underscores: ___")
        elif st.button("Predict"):
            masked_text = user_input.replace('___', '<mask>')
            predictions = FillMask(masked_text).predict()
            st.write("Top predictions:")
            for pred in predictions:
                st.write(f"{pred['sequence']} (score: {pred['score']:.4f})")