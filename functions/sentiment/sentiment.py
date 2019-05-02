#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:20:04 2019

@author: aibarra1
"""
from textblob import TextBlob

def getSentiment(event, context):
    text = event['data']
    sentimentList =""
    blob = TextBlob(text) 
    if blob.sentiment.polarity > 0:
        sentimentList = "Positive"
    elif blob.sentiment.polarity < 0:
        sentimentList ="Negative"
    else:
        sentimentList = "Neutral"
        
    return sentimentList