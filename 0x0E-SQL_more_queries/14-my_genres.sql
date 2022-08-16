-- A script that lists all genres from hbtn_0d_tvshows, and displays the numb
-- of shows linked to each
SELECT 	genre.name
FROM 	tv_genres genre 
		INNER JOIN tv_show_genres tvg 
			ON tvg.genre_id = genre.id
		INNER JOIN tv_shows tv ON tv.id = tvg.show_id
WHERE tv.title = 'Dexter'
ORDER BY genre.name;
