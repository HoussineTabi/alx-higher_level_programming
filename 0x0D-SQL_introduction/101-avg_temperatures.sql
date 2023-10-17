-- Displays the average temperature in Fahrenheit
-- By city ordered by descending order
SELECT `city`, AVG(`value`) AS `avg_temp`
GROUP BY `city` ORDER BY `avg_temp` DESC;
