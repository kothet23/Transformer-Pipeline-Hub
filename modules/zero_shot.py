from pipelines import ZeroShotClassification
from utils.file_handlers import extract_text
import streamlit as st
import pandas as pd

def show_zero_shot():
    st.subheader("Zero-Shot Classification")
    uploaded_file = st.file_uploader("Upload text to classify", type=["txt", "pdf", "docx"])
    input_text = st.text_area("Or enter text to classify", height=100)
    if uploaded_file:
        input_text = extract_text(uploaded_file)
    
    labels = st.text_input("Enter possible labels (comma separated)", 
                        "politics, sports, technology, entertainment")
    candidate_labels = [x.strip() for x in labels.split(",")]
    
    if input_text and candidate_labels:
        if st.button("Classify"):
            classifier = ZeroShotClassification(input_text, candidate_labels)
            result = classifier.predict()
            
            st.subheader("Classification Results")
            st.write(f"Predicted label: **{result['labels'][0]}**")
            
            df = pd.DataFrame({
                "Label": result['labels'],
                "Score": result['scores']
            })
            st.bar_chart(df.set_index("Label"))
            
            with st.expander("Detailed Results"):
                st.json(result)