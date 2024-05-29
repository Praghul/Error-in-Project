#Text Data Preprocessing Lib
import numpy as np
import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

import json
import pickle

words = []
classes = []
word_tags_list = []
ignore_words = [",", ".", "!", "?", "'s", "'m"]

train_data_file = open("intents.json").read()
intents = json.loads(train_data_file)

# function for appending stem words
def getstemwords(words,ignore_words):
    stemmed_words = []
    for word in words:
        if word not in ignore_words:
            w = stemmer.stem(word.lower())
            stemmed_words.append(w)
    return stemmed_words        



    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

#Create word corpus for chatbot
#def corpus(words,classes,word_tag_list,ignore_words):
for intent in intents:
        for pattern in intents["patterns"]:
            pattern_word = nltk.word_tokenize(pattern)
            words.extend(pattern_word)
            word_tags_list.append((pattern_word,intents["tag"]))
        if intent["tag"] not in classes:
            classes.append(intents["tag"])   
            stemmed_words = getstemwords(words,ignore_words)
print(stemmed_words)
print(classes)         
        
     
    


