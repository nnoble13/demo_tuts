from transformers import pipeline
from fastapi import FastAPI

app = FastAPI()
sentiment_analyzer = pipeline("sentiment-analysis", model='distilbert-base-uncased-finetuned-sst-2-english')

@app.get("/analyze")
def analyze(text: str):
    return sentiment_analyzer(text)[0]['label']

def init():
    if __name__ == "__main__":
        import sys

        if len(sys.argv) > 1:
            input_text = " ".join(sys.argv[1:])  # Combine arguments into a single string
            sentiment = analyze(input_text)
            print(f"Sentiment: {sentiment}")
        else:
            print("Usage: python your_script_name.py 'Your text here'")
m
