# day4_nlp_basics.py
# NLP preprocessing using NLTK

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Task 1: Sentence Tokenization

paragraph = "Artificial Intelligence is transforming industries. NLP is a key part of AI. Tokenization is the first NLP step."

sentences = sent_tokenize(paragraph)

print("Task 1: Sentence Tokenization")
print(sentences)
print()


# Task 2: Word Tokenization

words = word_tokenize(paragraph)

print("Task 2: Word Tokenization")
print(words)
print()


# Task 3: Stemming with Porter Stemmer

stemmer = PorterStemmer()
word_list = ["playing", "played", "plays", "happily", "studies"]

print("Task 3: Stemming")
for word in word_list:
    print(f"Original: {word} -> Stem: {stemmer.stem(word)}")
print()


# Task 4: Lemmatization with WordNet

lemmatizer = WordNetLemmatizer()
lemma_words = ["running", "cars", "better", "children", "feet"]

print("Task 4: Lemmatization")
for word in lemma_words:
    print(f"Original: {word} -> Lemma: {lemmatizer.lemmatize(word)}")
print()


# Task 5: Stemming vs Lemmatization Comparison

compare_words = ["running", "studies", "better", "playing", "cars"]

print("Task 5: Stem vs Lemma Comparison")
for word in compare_words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"Word: {word} | Stem: {stem} | Lemma: {lemma}")
print()


# Bonus Task:

print("Bonus Task: Lemmatization with POS='v'")
for word in ["running", "playing", "ate"]:
    print(f"Word: {word} -> Verb Lemma: {lemmatizer.lemmatize(word, pos='v')}")
