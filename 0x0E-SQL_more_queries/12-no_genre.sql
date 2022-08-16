-- A script that list all shows contained in hbtn_0d_tvshows without genere linked
SELECT t.title, IF(ISNULL(g.genre_id) = 1, 'NULL', g.genre_id) AS genre_id
FROM tv_shows t LEFT OUTER JOIN tv_show_genres g ON t.id = g.show_id 
WHERE g.genre_id IS NULL
ORDER BY t.title, g.genre_id;
