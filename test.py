from pipelines import *

print("Sentiment Analysis:")
print(SentimentAnalysis('I love sweets').predict())

print("\nFill Mask:")
print(FillMask("The capital of France is <mask>").predict())

print("\nNamed Entity Recognition:")
print(NER("Hugging Face is based in New York City.").predict())

print("\nQuestion Answering:")
print(QuestionAnswering(
    question="Where is Hugging Face based?",
    context="Hugging Face is a company based in New York City."
).predict())

print("\nSummarization:")
print(Summarization("Hugging Face is a company that provides natural language processing tools. It is widely used in both academia and industry for state-of-the-art NLP applications.").predict())

print("\nText Generation:")
print(TextGenerator("The future of AI is").predict())

print("\nTranslation (French to English):")
print(Translation("Je t'aime.").predict())

print("\nZero-Shot Classification:")
print(ZeroShotClassification(
    text="This is a document about politics.",
    candidate_labels=["sports", "politics", "technology"]
).predict())
