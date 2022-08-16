-- A script that lists all genres from hbtn_0d_tvshows, and displays the numb
SELECT tv.title, IF(ISNULL(genre.name) = 1, 'NULL', genre.name) AS name
FROM tv_shows tv
	LEFT JOIN tv_show_genres tvg
		ON tvg.show_id = tv.id
	LEFT JOIN tv_genres genre
		ON genre.id = tvg.genre_id
ORDER BY tv.title, genre.name;
