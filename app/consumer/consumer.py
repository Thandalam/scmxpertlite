"""The above code is importing the necessary libraries for the program to run.
"""
import os
import json
import sys
import pymongo
from kafka import KafkaConsumer
from dotenv import load_dotenv
load_dotenv()


# CLIENT = pymongo.MongoClient("mongodb+srv://Monika:moni@cluster0.rpwb686.mongodb.net/test")
DB = CLIENT['scmxpertlite']
DATA_STREAM = DB["devicedata"]

# TOPIC_NAME = "devicedata"
bootstrap_servers = "app-kafka-1:9092"

CLIENT = pymongo.MongoClient(os.getenv("mongodbUri"))
# DB = CLIENT['scmxpertlite']
# DATA_STREAM = DB["datastream"]

TOPIC_NAME = os.getenv("topic_name")
# bootstrap_servers = "localhost:9092"

try:
    CONSUMER = KafkaConsumer(TOPIC_NAME, bootstrap_servers=bootstrap_servers,\
                              auto_offset_reset='latest')
    for DATA in CONSUMER:
        try:
            DATA = json.loads(DATA.value)
            mdata = DATA_STREAM.insert_one(DATA)
        except json.decoder.JSONDecodeError:
            continue
except KeyboardInterrupt:
    sys.exit()





    

