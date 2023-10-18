-- lists all comedy shows in hbtn_0d_tv_shows.
-- records are ordered in a descending order show title

SELECT t.`title`
FROM `tv_shows` AS t
INNER `tv_show_genres` AS s
ON t.`id` = s.`show_id`
INNER JOIN `tv_genre` AS g
ON g.`id` = s.`genre_id`
WHERE g.`name` = "Comedy"
ORDER BY t.`title`;
