-- Creates the database hbtn_0d_usa and the table cities 
-- (in the database hbtn_0d_usa).

-- Creates database
CREATE database IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Create table called cities
CREATE table IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
