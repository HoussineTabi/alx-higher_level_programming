-- Lists all records of the second_table having a name value.
SELECT `score`, `name`
FROM `seocnd_table`
WHERE `name` != ""
ORDER BY `score` DESC
