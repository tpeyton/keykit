-- delete database if it already exists
DROP DATABASE IF EXISTS keykit;

-- create database if it doesn't already exist
CREATE DATABASE keykit;

-- grant permissions on database to new keyman user
GRANT ALL PRIVILEGES ON keykit.* to 'keyman'@'localhost' IDENTIFIED BY 'zooper$secret';

-- use the newly created keykit database
USE keykit;

-- create keystore table and related columns
CREATE TABLE keystore
( id INT(11) NOT NULL AUTO_INCREMENT,
  hostname VARCHAR(25),
  ip VARCHAR(15) NOT NULL,
  ssh_fingerprint VARCHAR(256),
  ssh_key VARCHAR(4096),
  creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT keystore_pk PRIMARY KEY (id)
);
