-- creates a database hbtn_0d_usa and a table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(id INT AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));