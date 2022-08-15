-- A scripts that creats the database hbtn_0d_usa and the table `states`
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
use htbn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);

