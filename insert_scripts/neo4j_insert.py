#
#	Assume dbms.security.auth_enabled=false in neo4j.conf
#
from py2neo import Graph, Node, Relationship
import os,glob,json

graph = Graph()

def commonTagsCount(x,y):
	return len(set(x) & set(y))

def commonTermsCount(x,y):
	return len(set(x.split()) & set(y.split()))

path = os.getcwd() + '/../data/*.json'
files = glob.glob(path)

videos = []
for file in files:
	with open(file) as f:
		videos.append(json.load(f))
videos = videos[:10]

tx = graph.begin()
nodes = []

for video in videos:
	v = Node("Video", name = video["videoInfo"]["id"],
		commentCount = video["videoInfo"]["statistics"]["commentCount"], 
		viewCount = video["videoInfo"]["statistics"]["viewCount"], 
		favoriteCount = video["videoInfo"]["statistics"]["favoriteCount"], 
		dislikeCount = video["videoInfo"]["statistics"]["dislikeCount"], 
		likeCount = int(video["videoInfo"]["statistics"]["likeCount"])
	)
	nodes.append(v)
	tx.create(v)

for i in range(len(videos)):
	print i
	u = videos[i]
	for j in range(i+1, len(videos)):
		v = videos[j]

		# For channelIds
		if u["videoInfo"]["snippet"]["channelId"] == v["videoInfo"]["snippet"]["channelId"]:
			a,b = nodes[i], nodes[j]
			r = Relationship(a, "SAME_CHANNEL", b, channel = u["videoInfo"]["snippet"]["channelTitle"])
			tx.create(r)

		# For common tags
		if "tags" in u["videoInfo"]["snippet"] and "tags" in v["videoInfo"]["snippet"]:
			count = commonTagsCount(u["videoInfo"]["snippet"]["tags"], v["videoInfo"]["snippet"]["tags"])
			if count > 0:
				a,b = nodes[i], nodes[j]
				r = Relationship(a, "COMMON_TAGS", b, n_tags = count)
				tx.create(r)

		# For common terms in description
		count = commonTermsCount(u["videoInfo"]["snippet"]["description"], v["videoInfo"]["snippet"]["description"])
		if count > 0:
			a,b = nodes[i], nodes[j]
			r = Relationship(a, "SIMILAR_DESC", b, n_similiar = count)
			tx.create(r)

tx.commit()




