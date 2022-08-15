-- A script that lists all the cities contained in the database hbtn_0d_usa
SELECT c.id as id, c.name as name, s.name as name
FROM cities as c
	LEFT JOIN states as s ON s.id = c.state_id;
