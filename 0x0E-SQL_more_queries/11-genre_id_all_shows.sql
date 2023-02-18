-- Import the database dump of hbtn_0d_tvshow
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;