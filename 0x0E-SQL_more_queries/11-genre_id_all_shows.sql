-- A script that lists all shows contained in the database hbtn_0d_tvshows
SELECT t.title, g.genre_id
FROM tv_shows t INNER JOIN tv_show_genres g ON IFNULL(t.id = g.show_id, 0)
ORDER BY t.title, g.genre_id;
