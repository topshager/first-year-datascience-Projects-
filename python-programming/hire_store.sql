drop database if exists hire_store;

create database  hire_store;

use hire_store;

create table if not exists Customer(
cusId INT PRIMARY KEY  AUTO_INCREMENT,
fName varchar(40) NOT NULL,
sName VARCHAR(40) NOT NULL,
address VARCHAR(40) NOT NULL,
phone VARCHAR(10) NOT NULL UNIQUE
)ENGINE=INODB;

create table if not exists Equipment(
eld INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
eName VARCHAR(15) NOT NULL,
typ VARCHAR(1) NOT NULL,
datAdded DATE NOT NULL
)ENGINE = INNODB;

create  table if not exists Transactions(
custId INT NOT NULL,
eld INT NOT NULL,
dateHired DATE NOT NULL,
dateReturn DATE 
)ENGINE = INNODB;