-- A script that lists all the cities contained in the database hbtn_0d_usa
SELECT	cities.id as id,
	cities.name as name,
	states.name as name
FROM cities
	JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
