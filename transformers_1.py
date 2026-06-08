from transformers import pipeline

# Load a pre-trained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Run it on a sentence
result = classifier("I am absolutely thrilled about this upcoming job interview!")
print(result)