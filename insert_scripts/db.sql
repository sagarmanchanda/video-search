CREATE DATABASE new_db;
USE new_db;
CREATE TABLE users(
	userid INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(200),
	password VARCHAR(200)
);
CREATE TABLE search_history(
	userid INT,
	search_query VARCHAR(200)
);
INSERT INTO users (username, password) VALUES ("sagar", "sagar");
