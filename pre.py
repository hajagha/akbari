"""
Created on Sat Jan 23 12:12:09 2021

@author: amir
"""


import pickle
import sys

import pandas as pd
import numpy as np

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import re

from textblob import TextBlob










sid = SentimentIntensityAnalyzer()


data = sys.argv[1]






def textPreProccess(tweet):
    
    clean = re.sub('[^a-zA-Z ]','',tweet)
    clean= re.sub(r"http\S+", "", clean)
    clean= re.sub(r"pic.\S+", "", clean)
    clean = re.sub(r"#\S+","",clean)
    tokenized_tweet = word_tokenize(clean)
    tokenize_clean =[]
    stemmed =[]
    for word in tokenized_tweet :
        if word not in stopwords.words() :
            tokenize_clean.append(word)
    for word in tokenize_clean :
        stemmed.append(word)
        stemmed.append(" ")
        
    return "".join(stemmed)
    




data =textPreProccess(data)





        
        


def text_blob_analyze_subjec(tweet):
     blob_semti = TextBlob(str(tweet))
     return blob_semti.sentiment[1]



def text_blob_analyze_polarity(tweet):
     blob_semti = TextBlob(str(tweet))
     return blob_semti.sentiment[0]
     

def vader_pol(tweet):
    
    point = sid.polarity_scores(tweet)
    return point['compound']

final_data =[]

final_data.append(text_blob_analyze_polarity(data))
final_data.append(text_blob_analyze_subjec(data))
final_data.append(vader_pol(data))



print(final_data)

    