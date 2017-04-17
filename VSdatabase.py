from pymongo import *

db_name = "newdb"
collection_name = "newcoll"

def get_video_by_id(video_id):
	client = MongoClient()
	db = client[db_name]
	videos = db[collection_name]
	video_object = videos.find_one({"videoInfo.id": video_id})
	client.close()
	return video_object
