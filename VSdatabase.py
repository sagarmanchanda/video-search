from pymongo import *
from py2neo import Graph
import MySQLdb
import json

def get_config():
	f = open("config.json", "r")
	doc = f.read()
	doc_json = json.loads(doc)
	f.close()
	return doc_json

def get_video_by_id(video_id):
	config = get_config()
	client = MongoClient()
	db = client[config['mongo']['db_name']]
	videos = db[config['mongo']['collection_name']]
	video_object = videos.find_one({"videoInfo.id": video_id})
	client.close()
	return video_object

def get_similiar_videos(video_id, n_videos = 1, n_common_tags = 1, n_similiar_desc = 1):
	graph = Graph()
	query = """
			MATCH (u:Video)-[ct:COMMON_TAGS]-(v:Video)
			WITH u,ct,v
			MATCH (u)-[sd:SIMILAR_DESC]-(v)
			WHERE u.name = \"%s\" AND ct.n_tags > %d AND sd.n_similiar > %d
			RETURN v.name AS id
			ORDER BY ct.n_tags DESC, sd.n_similiar DESC
			LIMIT %d
			""" % (video_id, n_common_tags, n_similiar_desc, n_videos)

	data = graph.data(query)	
	return map(lambda v: get_video_by_id(v["id"]), data)

def connect_to_mysql():
	config = get_config()
	db = MySQLdb.connect(config['mysql']['host'], config['mysql']['user'], config['mysql']['password'], config['mysql']['db_name'])
	return db

def execute_sql(sql_query):
	db = connect_to_mysql()
	cursor = db.cursor()
	cursor.execute(sql_query)
	return cursor