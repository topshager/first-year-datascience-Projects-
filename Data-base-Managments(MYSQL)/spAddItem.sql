/***************************************************************
- Author: Joshua singrew
- Date: 23 october 2023
- Filename: spAddItem.sql
- Description: This script  adds a item to specififc characters inventory 
****************************************************************/
USE mmorpg;
DROP PROCEDURE IF EXISTS spAddItem;
DELIMITER $$

CREATE PROCEDURE spAddItem(
IN pCharacterName VARCHAR(55),
IN pItemName VARCHAR(55),
IN pQuan INT
)
BEGIN
DECLARE vCharacterID INT;
DECLARE vItemID INT;
DECLARE vCurrentQuantity INT;

#-- Get the CharacterID based on the provided character name
SELECT CharacterID INTO vCharacterID
FROM Characters
WHERE CharacterName = pCharacterName;

#-- Get the ItemID based on the provided item name
SELECT ItemID INTO vItemID
FROM Items
WHERE Name_s = pItemName;

#-- Check if the character and item exist
IF vCharacterID IS NULL THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Character not found';
    
    INSERT INTO Errorss  (ErrorType,Description )
    VALUES ('NUll value ','Character not found in database');
    
END IF;

IF vItemID IS NULL THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Item not found';
        
    INSERT INTO Errorss  (ErrorType,Description )
    VALUES (' Item not found','No coresponding item value ');
END IF;

#-- Get the current quantity of the item in the character's inventory
SELECT Quantity INTO vCurrentQuantity
FROM Inventory
WHERE CharacterID = vCharacterID AND ItemID = vItemID;

#-- Check if there is enough space to add the item
IF vCurrentQuantity >= 8 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Inventory is full for this item';
      INSERT INTO Errorss  (ErrorType,Description )
       VALUES (' no space','No slots left for items');
ELSE
   # -- Add the item to the inventory (increment quantity)
    INSERT INTO Inventory (CharacterID, ItemID, Quantity)
    VALUES (vCharacterID, vItemID,pQuan)
    ON DUPLICATE KEY UPDATE Quantity = pQuan;
END IF;

END $$

DELIMITER ;

CALL spAddItem('zues', 'AK47','9');

select * from errorss;