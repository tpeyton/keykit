-- delete database if it already exists
DROP DATABASE IF EXISTS keykit;

-- create database
CREATE DATABASE keykit;

-- grant permissions on database to new keyman user. Note: change '%' wildcard remote ip address and the password before deploying in a real enviroment.
GRANT ALL PRIVILEGES ON keykit.* TO 'keyman'@'%' IDENTIFIED BY 'zooper$secret' REQUIRE SSL;

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
