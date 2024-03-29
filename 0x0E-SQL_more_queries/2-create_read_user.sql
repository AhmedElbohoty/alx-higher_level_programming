-- creates the database hbtn_0d_2 and the user user_0d_2.

-- Create new database called hbtn_0d_2
CREATE database IF NOT EXISTS hbtn_0d_2;

-- Create a new user called user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Add privilege to the user
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
