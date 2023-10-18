-- creates the database hbtn_0d_usa and the table states

create database if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
create table if not exists states
(id int unique not null default 1, name varchar(256) not null);
