-- This script prepares a MySQL server for the project.
-- Create a database for project development named: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user for project development at localhost named: hbnb_test
-- with password set to 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to the new user: hbnb_test.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Grant SELECT privilege on the database 'performance_schema'.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

