import nltk
import re

from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
text="nltk.tokenize.word_tokenize() tokenizes sentences into words, numbers and punctuation marks. It does not split words into syllables, but simply splits text at word boundaries."
tokens=word_tokenize(text)
print(tokens)

#whitespace tokenization
tokens1=text.split()
print(tokens1)

#Regex tokenization
s="Hello, I am working at X-Y-Z and my email is ZYX@gmail.com"
pattern=r'([\w]+-[\w]+-[\w]+)|([\w\.-]+@[\w]+\.[\w]+)'
print(re.findall(pattern,s))

#punctuation based tokenization
clean_text=re.sub(r'\W+',' ',s)
print(re.findall(r'\b\w+\b',clean_text))

#language based tokenization
import indicnlp 

from indicnlp.tokenize import indic_tokenize
print(list(indic_tokenize.trivial_tokenize(s,lang='en')))