-- create a table id_not_null on mysql

create table if not exists id_not_null
(id INT NOT NULL DEFAULT 1, name VARCHAR(256) NOT NULL);
