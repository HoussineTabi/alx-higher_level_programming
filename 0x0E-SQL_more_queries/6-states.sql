-- creates the database hbtn_0d_usa and the table states

create database if not exists hbtn_0d_usa;
create table if not exists hbtn_0d_usa.states
(id int unique not null AUTO_INCREMENT PRIMARY KEY, name varchar(256) not null);
