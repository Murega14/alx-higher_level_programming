-- lists all shows and all genres linked to a show
SELECT ts.title, tg.name FROM tv_shows AS tv_shows ts, tv_genres tg
LEFT JOIN tv_show_genres on ts.id = tv_show_genres.show_id
LEFT JOIN tg on tv_show_genres.genre_id = tg.id
ORDER BY ts.title, tg.name;