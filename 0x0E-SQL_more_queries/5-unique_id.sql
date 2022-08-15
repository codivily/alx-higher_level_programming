-- A script that create the table `unqieu_id`
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256),
	CONSTRAINT uk_id UNIQUE (id));
