-- A scripts that creats the database hbtn_0d_usa and the table `states`
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS htbn_0d_usa.states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256));
