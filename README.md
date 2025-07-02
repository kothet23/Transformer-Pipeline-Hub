# 🤗 Hugging Face Transformer Pipelines with Streamlit UI

This project provides an interactive **Streamlit web application** that demonstrates various **Hugging Face Transformers pipelines** using PyTorch (`framework='pt'`). The app offers an easy-to-use interface to explore powerful Natural Language Processing (NLP) models such as sentiment analysis, text generation, translation, and more.

---

## 🚀 Features

With this app, you can interactively try the following NLP tasks:

- **Sentiment Analysis** — Understand the sentiment (positive/negative) of a text.
![sentiment](https://github.com/user-attachments/assets/15d1b24b-1ea0-49b6-80ca-9b09a32d1ecd)
- **Fill-Mask** — Predict masked tokens in a sentence using masked language modeling.
![fill](https://github.com/user-attachments/assets/c792104d-d0ba-4071-aeb8-65b88cc89b50)
- **Named Entity Recognition (NER)** — Identify names, locations, and organizations.
![ner](https://github.com/user-attachments/assets/c9232659-3389-42c3-89ac-4d0b06ce0ce9)
- **Question Answering** — Answer questions based on a given context.
![qa](https://github.com/user-attachments/assets/c084f3ed-a9dc-490c-a633-734dc592f577)
- **Text Summarization** — Generate concise summaries of long texts.
![summerize](https://github.com/user-attachments/assets/34d6cc01-480c-4871-8cbb-b8b05e4e7bcc)
- **Text Generation** — Generate text from a prompt using autoregressive models.
![text_gen](https://github.com/user-attachments/assets/578ce894-66a7-4bab-88c0-ed3b634e90c4)
- **Translation (French → English)** — Translate French text into English.
![translate](https://github.com/user-attachments/assets/e98ffe6b-4833-4dfa-b6d9-f55b967bef01)
**Zero-Shot Classification** — Classify text without task-specific training.
![zero_shot](https://github.com/user-attachments/assets/79b94e0c-1cef-44a8-8152-ede6116bf6b1)

---

## Powered by Hugging Face Pipelines

Each task is powered by the `transformers.pipeline()` interface:

```python
from transformers import pipeline

classifier = pipeline('sentiment-analysis')
result = classifier("I love Streamlit and Transformers!")
