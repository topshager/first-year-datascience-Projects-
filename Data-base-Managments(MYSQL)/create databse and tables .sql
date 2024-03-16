/***************************************************************
* Author:   Joshua singrew
* Date:     23 october 2023
* Filename: Create Database and Tables.sql
* Description: This script creates the  MMORPG database and it's  associated tables 
****************************************************************/

#dropping and recreating  database 
DROP  DATABASE  IF EXISTS  MMORPG;
CREATE DATABASE MMORPG;

USE MMORPG;
# creating person  table 
CREATE TABLE Person(
PersonEmail VARCHAR(55)  UNIQUE NOT NULL PRIMARY KEY,
PersonName VARCHAR(55) NOT NULL
)ENGINE = InnoDB;
#creatin accounts table 
CREATE TABLE Accounts (
AccountID INT AUTO_INCREMENT PRIMARY KEY,
AccountName VARCHAR(55) UNIQUE NOT NULL,
ExpiryDate DATE,
IsBlocked BOOLEAN,
PersonEmail VARCHAR(55),
FOREIGN KEY (PersonEmail) REFERENCES Person(PersonEmail)
)ENGINE = InnoDB;
#creatin Characters table 
CREATE TABLE Characters (
CharacterID INT AUTO_INCREMENT PRIMARY KEY,
AccountID INT,
CharacterName VARCHAR(55) NOT NULL,
Team VARCHAR(55),
SkillLevel INT,
FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
)ENGINE = InnoDB;
#creatin Items table 
CREATE TABLE Items (
ItemID INT AUTO_INCREMENT PRIMARY KEY,
Name_s VARCHAR(55) NOT NULL,
Description TEXT
)ENGINE = InnoDB;
#creatin Inventory table 
CREATE TABLE Inventory (
InventoryID INT AUTO_INCREMENT PRIMARY KEY,
CharacterID INT,
ItemID INT,
Quantity INT,
FOREIGN KEY (CharacterID) REFERENCES Characters(CharacterID),
FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
)ENGINE = InnoDB;
#creatin Errorss table 
CREATE TABLE Errorss (
ErrorID INT AUTO_INCREMENT PRIMARY KEY,
ErrorType VARCHAR(255),
Description TEXT
)ENGINE = InnoDB;

 