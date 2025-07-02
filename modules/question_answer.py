from pipelines import QuestionAnswering
from utils.file_handlers import extract_text
import streamlit as st

def show_question_answer():
    st.subheader("Document Analysis Tool")
    uploaded_file = st.file_uploader("Upload Context (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
    if uploaded_file:
        context = extract_text(uploaded_file)
        with st.expander("View Context Text"):
            st.text(context[:5000] + ("..." if len(context) > 5000 else ""))
        question = st.text_input("Ask a question about the document:")
        if question:
            qa = QuestionAnswering(question=question, context=context)
            answer = qa.predict()
            st.subheader("Answer:")
            st.success(f"**{answer['answer']}** (Confidence: {answer['score']:.2f})")
            with st.expander("Detailed Results"):
                st.json(answer)
