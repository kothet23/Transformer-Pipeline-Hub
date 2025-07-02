import streamlit as st
from streamlit_option_menu import option_menu  

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    choice = option_menu(
        menu_title=None, 
        options=['Sentiment Analysis', 'Filling Mask', 'Named Entity Recognition',
                'Question Answering', 'Text Summarization', 'Text Generation',
                'Translation (French to English)', 'Zero-Shot Classification'],
        icons=['emoji-smile', 'mask', 'geo-alt', 'question-circle',
              'file-text', 'chat-left-text', 'translate', 'tags'],
        menu_icon=None,
        default_index=0,
        styles={
            "container": {"padding": "0"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0"},
        }
    )
 
left_space, main_container, right_space = st.columns([1, 2.5, 1])

with main_container:
    st.title('Hugging Face Transformer Pipelines')
    if choice == 'Sentiment Analysis':
        from modules.sentiment import show_sentiment_analysis
        show_sentiment_analysis()

    elif choice == 'Filling Mask':
        from modules.fill_mask import show_fill_mask
        show_fill_mask()
        
    elif choice == 'Named Entity Recognition':
        from modules.ner import show_NER
        show_NER()

    elif choice == 'Question Answering':
        from modules.question_answer import show_question_answer
        show_question_answer()
        
    elif choice == 'Text Summarization':
        from modules.summerize import show_summerization
        show_summerization()

    elif choice == 'Text Generation':
        from modules.text_generation import show_text_generation
        show_text_generation()

    elif choice == 'Translation (French to English)':
        from modules.translation import show_translation
        show_translation()

    elif choice == 'Zero-Shot Classification':
        from modules.zero_shot import show_zero_shot
        show_zero_shot()