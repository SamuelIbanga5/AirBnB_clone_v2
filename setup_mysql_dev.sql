-- This script prepares a MySQL server for the project.
-- Create a database for project development named: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user for project development at localhost named: hbnb_dev
-- with password set to 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the new user: hbnb_dev.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant SELECT privilege on the database 'performance_schema'.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

