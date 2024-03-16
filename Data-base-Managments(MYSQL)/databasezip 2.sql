USE mmorpg;

DROP  VIEW IF EXISTS vwTopStackedItems;
CREATE VIEW vwTopStackedItems AS
SELECT i.Name_s AS ItemName, COUNT(inv.ItemID) AS StackCount, GROUP_CONCAT(DISTINCT c.CharacterName ORDER BY c.CharacterName ASC) AS CharacterList
FROM Inventory inv
JOIN Items i ON i.ItemID = inv.ItemID
JOIN Characters c ON c.CharacterID = inv.CharacterID
GROUP BY i.Name_s
ORDER BY StackCount DESC
LIMIT 20;

SELECT * FROM vwTopStackedItems;

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

-- Get the CharacterID based on the provided character name
SELECT CharacterID INTO vCharacterID
FROM Characters
WHERE CharacterName = pCharacterName;

-- Get the ItemID based on the provided item name
SELECT ItemID INTO vItemID
FROM Items
WHERE Name_s = pItemName;

-- Check if the character and item exist
IF vCharacterID IS NULL THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Character not found';
END IF;

IF vItemID IS NULL THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Item not found';
END IF;

-- Get the current quantity of the item in the character's inventory
SELECT Quantity INTO vCurrentQuantity
FROM Inventory
WHERE CharacterID = vCharacterID AND ItemID = vItemID;

-- Check if there is enough space to add the item
IF vCurrentQuantity >= 8 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Inventory is full for this item';
ELSE
    -- Add the item to the inventory (increment quantity)
    INSERT INTO Inventory (CharacterID, ItemID, Quantity)
    VALUES (vCharacterID, vItemID,pQuan)
    ON DUPLICATE KEY UPDATE Quantity = pQuan;
END IF;

END $$

DELIMITER ;

CALL spAddItem('zues', 'AK47','9');

select * from inventory;