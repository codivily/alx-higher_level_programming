-- A script that lists all the cities contained in the database hbtn_0d_usa
SELECT c.id as id, c.name as name, s.name as name
FROM cities c
	LEFT OUTER JOIN states s ON s.id = c.state_id;
