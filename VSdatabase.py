from pymongo import *
from py2neo import Graph
import MySQLdb
import json
import imagehash
from PIL import Image

def loadThumbnailHashes():
	t = {}
	client = MongoClient()
	db = client['newdb']
	videos = db['newcoll']
	result = videos.find({}, {'thumbnailHash':1, 'videoInfo.id':1})
	client.close()
	for r in result:
		if 'thumbnailHash' not in r:
			r['thumbnailHash'] = '0'*16
		t[r['videoInfo']['id']] = r['thumbnailHash']
		
	return t

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

tHashMap = loadThumbnailHashes()

def find_similiar_thumbnail(image_path):
	image_hash = imagehash.average_hash(Image.open(image_path))

	videos = {}
	for k,v in tHashMap.items():
		h = imagehash.hex_to_hash(v)
		d = h - image_hash
		videos[k] = d

	data = sorted(videos, key = videos.get)[:5]
	return map(lambda v: get_video_by_id(v), data)

def connect_to_mysql():
	config = get_config()
	db = MySQLdb.connect(config['mysql']['host'], config['mysql']['user'], config['mysql']['password'], config['mysql']['db_name'])
	return db

def execute_sql(sql_query):
	db = connect_to_mysql()
	cursor = db.cursor()
	cursor.execute(sql_query)
	return cursor

def set_like_count(video_id, username):
	db = connect_to_mysql()
	cursor = db.cursor()
	col_name = get_colname_by_videoid(video_id)
	sql_query = """
				UPDATE likes SET %s = 1 WHERE username = \"%s\";  
				""" % (col_name, username)
	cursor.execute(sql_query)
	db.commit()
	db.close()

def get_colname_by_videoid(video_id):
	f = open('utility-dict.json', 'r')
	data = f.read()
	data = json.loads(data)
	return data[video_id+'.json']

def get_videoid_by_colname(col_name):
	f = open('utility-dict.json', 'r')
	data = f.read()
	data = json.loads(data)
	video_id = None
	for key in data:
		if data[key] == col_name:
			video_id = key
			break
	return video_id[:-5]

