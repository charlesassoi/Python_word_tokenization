import nltk

from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
text="nltk.tokenize.word_tokenize() tokenizes sentences into words, numbers and punctuation marks. It does not split words into syllables, but simply splits text at word boundaries."
tokens=word_tokenize(text)
print(tokens)