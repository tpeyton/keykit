-- create database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS keykit;

-- grant permissions on database to new keyman user
GRANT ALL PRIVILEGES ON keykit.* to keyman@'localhost' IDENTIFIED BY 'zooper$secret';

-- create table and columns
CREATE TABLE keystore
( id INT(11) NOT NULL AUTO_INCREMENT,
  hostname VARCHAR(25),
  ip VARCHAR(15) NOT NULL,
  ssh_fingerprint VARCHAR(1024),
  ssh_key VARCHAR(1024),
  creation_date DATE,
  CONSTRAINT keystore_pk PRIMARY KEY (id)
);
