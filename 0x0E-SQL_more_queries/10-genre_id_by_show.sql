-- Lists all shows contained in hbtn_0d_tvshows that have one gener linked.
-- Display all recoreds sorted

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
