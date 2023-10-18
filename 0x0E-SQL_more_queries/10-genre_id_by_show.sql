-- Lists all shows contained in hbtn_0d_tvshows that have one gener linked.
-- Display all recoreds sorted

select tv_shows.title, tv_show_genres.genre_id
from tv_shows
inner join tv_show_genres
on tv_shows.id=tv_show_genres.show_id
order by tv_shows.title, tv_show_genres.genre_id;
