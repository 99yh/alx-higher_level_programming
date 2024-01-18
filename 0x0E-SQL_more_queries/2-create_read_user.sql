-- create a user and grant them privileges

-- create db if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create a user @ the localhost mysql server
CREATE USER IF NOT EXISTS
user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- set privliges of user_0d_1
GRANT SELECT PRIVILEGES ON hbtn_0d_2.* TO user_0d_2@localhost;
