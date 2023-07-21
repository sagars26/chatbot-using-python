import random
import json
import pickle
import tensorflow as tf
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

intro= json.loads(open('intro.json').read())

words=[]
classes=[]
documents=[]
ignorel=['?','.',',','!']

for intent in intro['intro']:
    for pattern in intent['patterns']:
        wordlist=nltk.wordpunct_tokenize(patterns)
        words.extend(wordlist)
        documents.append((wordlist,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words=[lemma.lemmatize(word) for word in words if word not in ignorel]
 