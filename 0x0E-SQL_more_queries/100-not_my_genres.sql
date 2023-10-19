-- Converts the entire database hbtn_0c_0 to UTF8.
SELECT tg.name
FROM tv_genres tg
LEFT JOIN tv_shows ts ON ts.genre_id = tg.id
WHERE ts.title IS NULL OR ts.title <> 'Dexter'
ORDER BY tg.name;
