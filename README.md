# terminal-message-server-client
A simple example of messaging in a terminal via a server.
# Configuration DB
CREATE DATABASE testdb;

USE testdb;

CREATE TABLE user_tbl(id VARCHAR(20) NOT NULL , pass VARCHAR(40) NOT NULL);

CREATE TABLE message_tbl(id INT NOT NULL AUTO_INCREMENT,
user VARCHAR(20) NOT NULL, data VARCHAR(1400) NOT NULL,
sender VARCHAR(20) NOT NULL, PRIMARY KEY ( id ));
