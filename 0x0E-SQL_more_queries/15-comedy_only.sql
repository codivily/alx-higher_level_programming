-- A script that lists all genres from hbtn_0d_tvshows, and displays the numb
SELECT tv.title
FROM tv_shows tv
	INNER JOIN tv_show_genres tvg
		ON tvg.show_id = tv.id
	INNER JOIN tv_genres genre
		ON genre.id = tvg.genre_id
WHERE genre.name = 'Comedy'
ORDER BY tv.title;
