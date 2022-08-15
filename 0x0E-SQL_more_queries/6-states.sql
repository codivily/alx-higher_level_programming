-- A scripts that creats the database hbtn_0d_usa and the table `states`
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS htbn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	CONSTRAINT uk_states_id UNIQUE (id),
	CONSTRAINT pk_states PRIMARY KEY (id));

