-- lists all comedy shpws in the database
SELECT ts.title FROM tv_shows AS ts
INNER JOIN tv_show_genres ON ts.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY ts.title;