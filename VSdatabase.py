from pymongo import *
from py2neo import Graph

db_name = "newdb"
collection_name = "newcoll"

def get_video_by_id(video_id):
	client = MongoClient()
	db = client[db_name]
	videos = db[collection_name]
	video_object = videos.find_one({"videoInfo.id": video_id})
	client.close()
	return video_object

def get_similiar_videos(video_id, n_videos = 1, n_common_tags = 1, n_similiar_desc = 1):
	graph = Graph()
	query = """
			MATCH (u:Video)-[ct:COMMON_TAGS]-(v:Video)
			WITH u,ct,v
			MATCH (u)-[sd:SIMILAR_DESC]-(v)
			WHERE u.name = %s AND ct.n_tags > %d AND sd.n_similiar > %d
			RETURN v.name AS id
			ORDER BY ct.n_tags DESC, sd.n_similiar DESC
			LIMIT %d
			""" % (video_id, n_common_tags, n_similiar_desc, n_videos)

	data = graph.data(query)	
	return map(lambda v: get_video_by_id(v["id"]), data)
