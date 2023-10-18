-- creates the table unique_id on Mysql server

create table if not exists unique_di
(id int unique default 1, name varchar(256) not null);
