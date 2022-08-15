SELECT tv.title as title,
	tvgenre.genre_id as genre_id
FROM tv_shows tv
	LEFT OUTER JOIN tv_show_genres tvgenre ON tvgenre.show_id = tv.id
WHERE genre_id IS NOT NULL
ORDER BY title, genre_id;
