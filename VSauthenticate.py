import MySQLdb
from VSdatabase import *

def check_user(username, password):
	found_user = False
	user_id = None
	db = connect_to_mysql()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM users")
	for row in cursor.fetchall():
		if username==row[1] and password==row[2]:
			found_user = True
			user_id = row[0]
			break
	db.close()
	return found_user, user_id

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
	
	db.close()
	return user_added

# add_user("test", "test")