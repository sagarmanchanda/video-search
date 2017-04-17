import os
import json

def preprocess(search_query):
	
	db_name = "newdb"
	coll_name = "newcoll"
	query_text = 'db.' + coll_name + '.find({$text: {$search: "'+ search_query + '"}}, {score: {$meta: "textScore"}}).sort({score:{$meta:"textScore"}}).limit(10);\n'

	f = open("temp/query.js", "w+")
	f.write("use " + db_name + ";\n")
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
