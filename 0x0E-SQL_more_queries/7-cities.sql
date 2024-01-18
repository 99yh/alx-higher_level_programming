-- create a user and grant them privileges

-- create db if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- cd into the db
USE hbtn_0d_usa;

-- create table if not exists
CREATE TABLE IF NOT EXISTS city (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256),
	state_id INT NOT NULL,
	FOREIGN KEY (state_id)
		REFERENCES states(id)
);
