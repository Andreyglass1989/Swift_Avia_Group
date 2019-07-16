import nltk
from nltk.book import *

text1.concordance("monstrous")









from nltk import word_tokenize



text_hello="Привет мир. Я люблю программирование, и не только. Замечательный мир, он яркий и красивый."
'''
>>> type(text_hello)
<type 'str'>
'''
text_hello=text_hello.decode('utf8')
tokens = word_tokenize(text_hello)
'''
>>> type(tokens)
<type 'list'>
'''
len(tokens)
text = nltk.Text(tokens)