import os
import json
import pymongo
from pymongo import MongoClient

path = "data/"

client = MongoClient()
db = client['newdb']
collection = client['newcoll']

for filename in os.listdir(path):
    file = open(path+filename, 'r')
    document = file.read()
    doc_json = json.loads(document)
    doc_json['videoInfo']['statistics']['likeCount'] = int(doc_json['videoInfo']['statistics']['likeCount']) 
    result = db.newcoll.insert_one(doc_json)
    print result
