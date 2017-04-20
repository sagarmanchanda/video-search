import os
import json
from VSdatabase import *
from collections import OrderedDict

def preprocess(search_query):
	config = get_config()
	search_query = search_query.replace('\"', '\\\"')
	query_text = 'db.' + config['mongo']['collection_name'] + '.find({$text: {$search: "'+ search_query + '"}}, {score: {$meta: "textScore"}}).sort({score:{$meta:"textScore"}}).limit(10);\n'

	f = open("temp/query.js", "w+")
	f.write("use " + config['mongo']['db_name'] + ";\n")
	f.write(query_text)
	f.close()

def delete_temp_files():
	os.remove("temp/query.js")
	os.remove("temp/result.txt")
	os.remove("temp/result.json")

def clean_data():
	f = open("temp/result.txt", "r")
	lines = f.readlines()
	lines = lines[4:-1]
	f.close()
	f = open("temp/result.json", "w+")
	for line in lines:
		f.write("{" + line[47:])
	f.close()


def find_results(search_query):
	result = []
	preprocess(search_query)
	os.system('mongo < temp/query.js > temp/result.txt')
	clean_data()
	f = open("temp/result.json")
	lines = f.readlines()
	for line in lines:
		result.append(json.loads(line))
	delete_temp_files()

	return result

def collab_recommendation(username, number_of_results):
	db = connect_to_mysql()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM likes")
	recommendation_matrix = {}
	user_rank = {}
	video_rank = {}
	for row in cursor.fetchall():
		recommendation_matrix[row[0]] = row[:]
		user_rank[row[0]] = 0

	videos_liked_by_user = []
	for x in range(1,501):
		video_rank[x] = 0
		if recommendation_matrix[username][x] == 1:
			videos_liked_by_user.append(x)

	for video in videos_liked_by_user:
		for key in recommendation_matrix:
			if recommendation_matrix[key][video] == 1:
				user_rank[key] += 1

	user_rank[username] = -1
	user_rank_sorted = OrderedDict(sorted(user_rank.items(), key=lambda x: x[1]))

	for x in range(1,501):
		score = 0
		for key in user_rank_sorted:
			if recommendation_matrix[key][x] == 1:
				video_rank[x] += score
			score += 3

	video_rank_sorted = OrderedDict(sorted(video_rank.items(), key=lambda x: x[1], reverse=True))

	result = []
	for key in video_rank_sorted:
		result.append(get_video_by_id(get_videoid_by_colname("vid"+str(key))))

	return result[:number_of_results]