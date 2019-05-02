#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 2 2019

@author: aibarra1
@author: juliocri
"""
from textblob import TextBlob
from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from uuid import uuid

def getSentimentKafka(event, context):
    text = event['data']
    sentimentList =""
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        sentimentList = "Positive"
    elif blob.sentiment.polarity < 0:
        sentimentList ="Negative"
    else:
        sentimentList = "Neutral"

    producer = KafkaProducer(
    bootstrap_servers=['localhost:30092'],
    value_serializer=lambda x: dumps(x).encode('utf-8'))
    messageId = uuid.uuid4()
    data = {'id': messageId, 'sentiment': sentimentList}
    producer.send('test', value=data)
    sleep(5)

    consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['localhost:30092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
    message = message.value
    print('{} message was read!'.format(message))

    return sentimentList
