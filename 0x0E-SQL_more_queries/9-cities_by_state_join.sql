-- A script that lists all the cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM cities AS c INNER JOIN states AS s ON s.id = c.state_id;
