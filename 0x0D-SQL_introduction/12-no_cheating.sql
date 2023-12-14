-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- create a new table
UPDATE second_table
   SET score = 10
 WHERE name = "Bob";
