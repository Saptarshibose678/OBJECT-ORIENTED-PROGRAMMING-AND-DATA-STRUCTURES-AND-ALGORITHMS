create database password_manager;

use password_manager;

create table website_passwords (user_id int auto_increment primary key, username varchar(255), web_password varchar(255),
website_name varchar(255), website_url varchar(255), created_data varchar(255), last_updated_date varchar(255));


create table desktop_passwords (user_id_desktop int auto_increment primary key, username varchar(255), app_password varchar(255),
app_name varchar(255), created_data varchar(255), last_updated_date varchar(255));


create table game_passwords (user_id_game int auto_increment primary key, username varchar(255), game_password varchar(255),
game_name varchar(255), game_developer varchar(255), created_data varchar(255), last_updated_date varchar(255));

