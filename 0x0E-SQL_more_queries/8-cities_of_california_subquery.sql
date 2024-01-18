-- list all cities in the California state
-- select and condition is the primary key
SELECT *
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
);
