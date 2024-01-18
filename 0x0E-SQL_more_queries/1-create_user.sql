-- create a user and grant them privileges

-- create a user @ the localhost mysql server
CREATE USER IF NOT EXISTS
user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd;

-- set privliges of user_0d_1
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
