-- A script that lists all shows contained in the database hbtn_0d_tvshows
SELECT t.title, IF(ISNULL(g.genre_id), 'NULL', g.genre_id) as genre_id
FROM tv_shows t INNER JOIN tv_show_genres g ON t.id = g.show_id 
ORDER BY t.title, g.genre_id;
