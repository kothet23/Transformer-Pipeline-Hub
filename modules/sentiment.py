from pipelines import SentimentAnalysis
from utils.file_handlers import extract_text
import streamlit as st

def show_sentiment_analysis():
    st.subheader("Sentiment Analysis")
    uploaded_file = st.file_uploader("Upload a text file", type=["txt", "pdf", "docx"])
    input_text = st.text_input('Or enter text below')
    
    if uploaded_file:
        input_text = extract_text(uploaded_file)
        
    if input_text and st.button('Analyze'):
        pred = SentimentAnalysis(input_text).predict()
        st.write(f"Label : {pred[0]['label']}")
        st.write(f"Score : {pred[0]['score']}")