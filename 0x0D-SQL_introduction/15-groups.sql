-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- show the average of all scores
SELECT score, COUNT() AS `number`
  FROM second_table
 GROUP BY score
 ORDER BY score DESC;
