from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def summarize(self, text):
        return self.summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
