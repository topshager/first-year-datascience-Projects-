/***************************************************************

- Author: Joshua singrew
- Date: 23 october 2023
- Filename: Trigger .sql
- Description: This script  creates triggers for mmorpg
****************************************************************/


USE MMORPG;

DELIMITER $$

CREATE TRIGGER  user_count AFTER INSERT  ON PERSON#--create trigger

FOR EACH ROW
BEGIN
declare user_count int;
set user_count  = user_count + 1;#--count number of users after registraton 

END$$


USE MMORPG;
DELIMITER $$
CREATE  TRIGGER CHECK_QUANT  BEFORE INSERT  ON Inventory
FOR EACH ROW
BEGIN
IF NEW.Quantity > 99 THEN#--set maximum limit  for number  items added to inventory 
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'ERROR: Quantity can not be more than 99';#-- rais error
END IF ;
END$$


