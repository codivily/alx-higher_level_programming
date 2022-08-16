-- A script that lists all genres from hbtn_0d_tvshows, and displays the numb
-- of shows linked to each
SELECT 	genre.name AS genre,
	SUM(IF(ISNULL(tvg.show_id), 0, 1)) AS number_of_shows
FROM 	tv_genres genre 
		LEFT JOIN tv_show_genres tvg 
			ON tvg.genre_id = genre.id
GROUP BY genre.name
ORDER BY number_of_shows DESC;
