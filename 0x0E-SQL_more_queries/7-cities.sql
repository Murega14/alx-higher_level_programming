-- creates a database and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(id INT AUTO_INCREMENT, state_id INT AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY(id), FOREIGN KEY(state_id));