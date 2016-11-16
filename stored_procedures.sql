DELIMITER // 
DROP PROCEDURE IF EXISTS get_comics //
DROP PROCEDURE IF EXISTS get_issue //
DROP PROCEDURE IF EXISTS delete_issue //
DROP PROCEDURE IF EXISTS update_issue //
DROP PROCEDURE IF EXISTS add_new_issue //
DROP PROCEDURE IF EXISTS get_comics_by_series // 
DROP PROCEDURE IF EXISTS get_comics_by_publisher //
DROP PROCEDURE IF EXISTS get_comics_by_writer // 

DROP PROCEDURE IF EXISTS get_writers //
DROP PROCEDURE IF EXISTS add_new_writer // 
DROP PROCEDURE IF EXISTS get_writer // 
DROP PROCEDURE IF EXISTS update_writer //

DROP PROCEDURE IF EXISTS get_publishers // 
DROP PROCEDURE IF EXISTS add_new_publisher // 
DROP PROCEDURE IF EXISTS get_publisher // 
DROP PROCEDURE IF EXISTS update_publisher//

DROP PROCEDURE IF EXISTS get_series//
DROP PROCEDURE IF EXISTS add_new_series //
DROP PROCEDURE IF EXISTS get_specific_series //
DROP PROCEDURE IF EXISTS update_series //



CREATE PROCEDURE get_comics(IN i_user_id VARCHAR(255))
BEGIN 
	SELECT * FROM comic_issues WHERE user_id = i_user_id ORDER BY series_id ASC, issue_number ASC;
END // 

CREATE PROCEDURE get_issue (IN i_issue_id INT)
BEGIN 
	SELECT * FROM comic_issues WHERE id = i_issue_id;
END //

CREATE PROCEDURE delete_issue (IN i_issue_id INT)
BEGIN 
	DELETE FROM comic_issues WHERE id = i_issue_id;
END //

CREATE PROCEDURE update_issue (	IN i_issue_id INT, IN i_issue_number INT, IN i_series_id INT, IN i_grade float, IN i_image_url VARCHAR(255), IN i_writer_id INT, IN i_user_id VARCHAR(255), IN i_month INT, IN i_year INT)
BEGIN 
	UPDATE comic_issues SET series_id = i_series_id, issue_number = i_issue_number, grade = i_grade, image_url = i_image_url, writer_id = i_writer_id, user_id = i_user_id, month = i_month, year = i_year WHERE id = i_issue_id;
END //

CREATE PROCEDURE add_new_issue (IN i_issue_number INT,IN i_series_id INT, IN i_grade float, IN i_image_url VARCHAR(255), IN i_writer_id INT, IN i_user_id VARCHAR(255),IN i_month INT, IN i_year INT)
BEGIN 
	INSERT INTO comic_issues (series_id, issue_number, grade, image_url, writer_id, user_id, month, year) VALUES(i_series_id, i_issue_number, i_grade, i_image_url, i_writer_id, i_user_id, i_month, i_year);
END // 

CREATE PROCEDURE get_comics_by_series(	IN i_user_id VARCHAR(255), IN i_series_id INT)
BEGIN 
	SELECT * FROM comic_issues WHERE user_id = i_user_id AND series_id = i_series_id ORDER BY issue_number ASC;
END // 

CREATE PROCEDURE get_comics_by_publisher(	IN i_user_id VARCHAR(255), IN i_publisher_id INT)
BEGIN 
	SELECT * FROM comic_issues JOIN series ON series.id = comic_issues.series_id WHERE user_id = i_user_id AND series.publisher_id = i_publisher_id ORDER BY series_id ASC, issue_number ASC;
END // 

CREATE PROCEDURE get_comics_by_writer(IN i_user_id VARCHAR(255), IN i_writer_id INT)
BEGIN 
	SELECT * FROM comic_issues WHERE user_id = i_user_id AND writer_id = i_writer_id ORDER BY series_id ASC, issue_number ASC;
END // 



CREATE PROCEDURE get_writers()
BEGIN 
	SELECT * FROM writers;
END //

CREATE PROCEDURE add_new_writer (	IN i_first_name VARCHAR(255),IN i_last_name VARCHAR(255))
BEGIN 
	INSERT INTO writers (first_name, last_name) 
	VALUES(i_first_name, i_last_name);
END // 

CREATE PROCEDURE get_writer(IN i_writer_id INT)
BEGIN 
	SELECT * FROM writers WHERE id = i_writer_id;
END //

CREATE PROCEDURE update_writer (IN i_writer_id INT,IN i_first_name VARCHAR(255), IN i_last_name VARCHAR(255))
BEGIN 
	UPDATE writers SET first_name = i_first_name, last_name = i_last_name WHERE id = i_writer_id;
END //



CREATE PROCEDURE get_publishers()
BEGIN 
	SELECT * FROM publishers;
END //

CREATE PROCEDURE add_new_publisher (IN i_name VARCHAR(255))
BEGIN 
	INSERT INTO publishers (name) 
	VALUES(i_name);
END // 

CREATE PROCEDURE get_publisher(IN i_publisher_id INT)
BEGIN 
	SELECT * FROM publishers WHERE id = i_publisher_id;
END //

CREATE PROCEDURE update_publisher(	IN i_publisher_id INT,
									IN i_name VARCHAR(255))
BEGIN 
	UPDATE publishers SET name  = i_name WHERE id = i_publisher_id;
END //



CREATE PROCEDURE get_series()
BEGIN 
	SELECT * FROM series;
END //

CREATE PROCEDURE add_new_series(IN i_name VARCHAR(255),IN i_first_issue INT, IN i_last_issue INT, IN i_start_year INT, IN i_end_year INT,IN i_publisher_id INT)
BEGIN
	INSERT INTO series(name, first_issue, last_issue, start_year, end_year, publisher_id) VALUES (i_name, i_first_issue, i_last_issue, i_start_year, i_end_year, i_publisher_id);
END // 

CREATE PROCEDURE get_specific_series(IN i_series_id INT)
BEGIN
	SELECT * FROM series where id = i_series_id;
END //

CREATE PROCEDURE update_series(	IN i_series_id INT, IN i_name VARCHAR(255), IN i_first_issue INT, IN i_last_issue INT, IN i_start_year INT, IN i_end_year INT, IN i_publisher_id INT)
BEGIN
	UPDATE series SET name = i_name, first_issue = i_first_issue, last_issue = i_last_issue, start_year = i_start_year, end_year = i_end_year, publisher_id = i_publisher_id WHERE id = i_series_id;
END //

DELIMITER ;
 
