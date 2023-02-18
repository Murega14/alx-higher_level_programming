--lists all genres from hbtn_od_tvshows and order by tv_show count
SELECT tgs.name AS genre, COUNT(TG.genre_id) AS number_shows
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
LEFT JOIN tv_genres AS tgs
ON tg.genre_id = tgs.id
WHERE tg.genre_id IS NOT NULL
GROUP BY tgs.name ORDER BY number_shows DESC;