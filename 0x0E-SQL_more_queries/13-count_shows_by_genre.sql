-- lists and shows to each all genres
-- orders records by descending number

SELECT g.`name` AS `genre`,
COUNT(*) AS `genre`,
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS t
ON g.`id` = t.`genre_id`
ORDER BY `number_of_shows` DESC;
