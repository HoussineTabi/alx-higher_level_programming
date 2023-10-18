-- cities of a
SELECT id, name FROM cities 
where state_id = (Select id from states where name = "California")
order by id;
