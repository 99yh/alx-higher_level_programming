-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- create a new table
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
