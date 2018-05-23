/* Create The Database */

DROP DATABASE IF EXISTS `automated_warehouse_management`;

CREATE DATABASE `automated_warehouse_management`;

/* Change To automated_warehouse_management Database */

use `automated_warehouse_management`;

/* Create Tables */

DROP TABLE IF EXISTS `storage_unit`;

CREATE TABLE `storage_unit` (
		id INT NOT NULL AUTO_INCREMENT,
		storage_unit_name CHAR(15) NOT NULL,
		no_of_items INT NOT NULL,
		max_capacity INT NOT NULL,
		PRIMARY KEY(id)
);

DROP TABLE IF EXISTS `sensor_data`;

CREATE TABLE `sensor_data` (
	id INT NOT NULL AUTO_INCREMENT,
	time_stamp TIMESTAMP NOT NULL,
	humidity float,
	temperature float,
	PRIMARY KEY(id)
);

DROP TABLE IF EXISTS `ev3_robot`;

CREATE TABLE `ev3_robot` (
	id INT NOT NULL AUTO_INCREMENT,
	time_stamp TIMESTAMP NOT NULL,
	job_id INT NOT NULL,
	status CHAR(15) NOT NULL,
	ev3_position CHAR(15),
	PRIMARY KEY(id)
);

/* Hack To Bypass Column Cannot Be NULL Error Caused By The Job_id_trigger */

INSERT INTO `ev3_robot`
	(job_id, status) 
VALUES
	(0, 'Testing'),
	(0, 'Done');

/* Create a Trigger To Auto Increment The JOB_ID After The Previous Job's Status Changes To Done */

DROP TRIGGER IF EXISTS `job_id_trigger`;

DELIMITER $$
CREATE TRIGGER `job_id_trigger` BEFORE INSERT ON `ev3_robot` FOR EACH ROW
BEGIN
	DECLARE prev_job_id INT;

	SELECT job_id
	INTO prev_job_id
	FROM ev3_robot
	WHERE status = 'Done'
	ORDER BY time_stamp DESC
	LIMIT 1;

	set NEW.job_id=(prev_job_id) + 1;
END $$

DELIMITER ;
