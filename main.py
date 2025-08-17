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

#wordpiece tokenization
from transformers import BertTokenizer
tokenizer=BertTokenizer.from_pretrained('bert-base-uncased')
def simple_tokenize(text):
    print(f"original text:{text}")


    #convert word to wordpiece tokens
    tokens=tokenizer.tokenize(s)
    print(f"wordpiece tokens{tokens}")

    #convert tokens to numerical IDs
    token_IDs=tokenizer.convert_tokens_to_ids(tokens)
    print(f"token_ids{token_IDs}")

    words=text.split
    print("\n word breakdown")
    for word in words:
        word_tokens=tokenizer.tokenize(word)
        print("f: {word} -> {word_tokens}")
simple_tokenize(s)