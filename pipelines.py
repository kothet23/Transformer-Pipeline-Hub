from transformers import pipeline

class SentimentAnalysis:
    def __init__(self, text):
        self.text = text 
    def predict(self):
        clf = pipeline('sentiment-analysis',framework='pt')
        return clf(self.text)

class FillMask:
    def __init__(self, text):
        self.text = text 
    def predict(self):
        model = pipeline('fill-mask',framework='pt')
        return model(self.text)
    
class NER:
    def __init__(self, text):
        self.text = text 
    def predict(self):
        model = pipeline('ner',grouped_entities=True,framework='pt')
        return model(self.text)
    
class QuestionAnswering:
    def __init__(self, question, context):
        self.question = question
        self.context = context
    def predict(self):
        model = pipeline('question-answering',framework='pt')
        return model(
            question=self.question,
            context=self.context
        )
    
class Summarization:
    def __init__(self, text):
        self.text = text
    def predict(self):
        model = pipeline('summarization',framework='pt')
        return model(self.text)
        
class TextGenerator:
    def __init__(self, text, max_length=100):
        self.text = text
        self.max_length = max_length
    def predict(self):
        model = pipeline('text-generation', max_length=self.max_length,framework='pt')
        return model(self.text)
           
class Translation:
    def __init__(self, text):
        self.text = text
    def predict(self):
        model = pipeline('translation', model="Helsinki-NLP/opus-mt-fr-en",framework='pt')
        return model(self.text)
    
class ZeroShotClassification:
    def __init__(self, text, candidate_labels):
        self.text = text
        self.candidate_labels = candidate_labels
    def predict(self):
        model = pipeline('zero-shot-classification',framework='pt')
        return model(
            self.text,
            candidate_labels=self.candidate_labels
        )
         


