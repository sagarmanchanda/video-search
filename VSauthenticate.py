import MySQLdb
from VSdatabase import *

def check_user(username, password):
	found_user = False
	db = connect_to_mysql()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM users")
	for row in cursor.fetchall():
		if username==row[0] and password==row[1]:
			found_user = True
			break
	db.close()
	return found_user

def add_user(username, password):
	user_added = False
	db = connect_to_mysql()
	cursor = db.cursor()
	sql_query = """
				INSERT INTO users (username, password) VALUES (\"%s\", \"%s\");  
				""" % (username, password)
	try:
		cursor.execute(sql_query)
		db.commit()
		user_added = True
	except:
		db.rollback()
	
	if user_added:
		sql_query = """
				INSERT INTO likes (username) VALUES (\"%s\");  
				""" % (username)
		cursor.execute(sql_query)
		db.commit()

	db.close()
	return user_added