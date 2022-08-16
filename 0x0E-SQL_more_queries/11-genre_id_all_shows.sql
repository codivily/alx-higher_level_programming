-- A script that lists all shows contained in hbtn_0d_tvshows database
SELECT t.title, IF(ISNULL(g.genre_id) = 1, 'NULL', g.genre_id) AS genre_id
FROM tv_shows t INNER JOIN tv_show_genres g ON t.id = g.show_id ORDER BY t.title, g.genre_id;
