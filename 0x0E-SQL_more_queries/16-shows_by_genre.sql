-- Lists all shows and linked to the show from the database
-- records must be ordered by ascending show title and genre

SELECT t.`title`, g.`name`
FROM `tv_shows` AS t
LEFT `tv_show_genres` AS s
ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS g
ON s.`genre_id` = g.`id`
ORDER BY t.`title`, g.`name`;
