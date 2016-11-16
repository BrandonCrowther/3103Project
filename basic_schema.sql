DROP TABLE comic_issues;
DROP TABLE writers;
DROP TABLE series;
DROP TABLE publishers;

CREATE TABLE publishers(
	id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(255) NOT NULL, 
	CONSTRAINT pk_publisherID PRIMARY KEY (id)
);
COMMIT; 
CREATE TABLE series(
	id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(255) NOT NULL, 
	first_issue int NOT NULL,
	last_issue int, 
	start_year int NOT NULL, 
	end_year int, 
	publisher_id int NOT NULL, 
	CONSTRAINT pk_seriesID PRIMARY KEY (id),
	CONSTRAINT CHECK (start_year>1900),
	CONSTRAINT CHECK (end_year > 1900),
	CONSTRAINT fk_seriesID FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);
COMMIT; 
CREATE TABLE writers(
	id INT NOT NULL AUTO_INCREMENT, 
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	CONSTRAINT pk_writersID PRIMARY KEY (id)
);
COMMIT;
CREATE TABLE comic_issues(
	id INT NOT NULL AUTO_INCREMENT, 
	series_id int NOT NULL,
	issue_number int NOT NULL, 
	grade float,
	image_url VARCHAR(255),
	writer_id int,
	user_id VARCHAR(255) NOT NULL,
	month int, 
	year int, 
	CONSTRAINT pk_issuesID PRIMARY KEY (id),
	CONSTRAINT fk_cissues1 FOREIGN KEY (series_id) REFERENCES series(id),
	CONSTRAINT fk_cissues2 FOREIGN KEY (writer_id) REFERENCES writers(id)
);
COMMIT;
