import os
from pymongo import MongoClient
from PIL import Image
import imagehash

path = "data/"

client = MongoClient()
db = client['newdb']
collection = client['newcoll']

def compute_image_hash(video_id):
	return imagehash.average_hash(Image.open('images/' + video_id + '.jpg'))

for filename in os.listdir(path):
    video_id = filename.split('.')[0]
    thumbnail_hash = str(compute_image_hash(video_id))
    result = db.newcoll.update_one({'videoInfo.id': str(video_id) }, {"$set": {"thumbnailHash" : thumbnail_hash}})

client.close()
