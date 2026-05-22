from collections import Counter
import re

text = """
Python is amazing. Python is fast, flexible, and powerful. 
Data science relies heavily on Python, and machine learning does too.
"""

# Clean the text: convert to lowercase and remove punctuation using regex
cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

# Split into individual words
words = cleaned_text.split()

print(words)

# Feed the list of words directly into Counter
word_counts = Counter(words)

print("\n--- Word Frequencies ---")
print(word_counts)

# Grab the top 3 most common words
print("\nTop 3 most common words:")
for word, count in word_counts.most_common(3):
    print(f"'{word}': {count} times")