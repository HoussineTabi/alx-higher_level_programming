-- lists all scores that greater than or equal 10
-- ordered by descending score
SELECT `score`, `name` 
FROM `second_table` 
WHERE `socre` >= 10 
ORDER BY `score` DESC;
