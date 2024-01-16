-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- create a new record in a table
INSERT
  INTO first_table
		(id, name)
VALUES	(89, 'Best School')
