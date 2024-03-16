/***************************************************************
- Author: Joshua singrew
- Date: 23 october 2023
- Filename: spRegister .sql
- Description: This script adds new  account 
****************************************************************/
USE mmorpg;

DELIMITER $$

DROP PROCEDURE IF EXISTS mmorpg.spRegister $$

CREATE PROCEDURE mmorpg.spRegister (
IN account_name VARCHAR(55),
in Person_Email VARCHAR(55)
)
BEGIN
IF NOT EXISTS (SELECT 1 FROM Accounts WHERE AccountName = account_name) THEN
INSERT INTO Accounts (AccountName,  PersonEmail)
VALUES (account_name, Person_Email);
ELSE
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Account name already exists';

INSERT INTO Errorss  (ErrorType,Description )#--insert errors details into  error table 
VALUES ('Existing value ','Account name already exists');
END IF;
END$$

DELIMITER ;;

CALL spRegister('MOOL,','lakaaka@gmail.com');

SELECT *
FROM accounts;