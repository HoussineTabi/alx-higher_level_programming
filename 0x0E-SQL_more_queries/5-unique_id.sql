-- creates the table unique_id on Mysql server

create table if not exists unique_id
(id int not null default 1 unique, name varchar(256) not null);
