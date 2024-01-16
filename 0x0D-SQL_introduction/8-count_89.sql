-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- get the total number of records with an id == 89
SELECT COUNT(id)
  FROM first_table
 WHERE id = 89;
