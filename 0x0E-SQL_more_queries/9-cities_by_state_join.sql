-- list all cities in the California state
-- select and condition is the primary key
SELECT cities.id, cities.name, states.name
  FROM cities
 INNER
	JOIN states
    ON cities.state_id = states.id
 ORDER BY id;
