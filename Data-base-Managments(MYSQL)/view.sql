
/***************************************************************

- Author: Joshua singrew
- Date: 23 october 2023
- Filename: View .sql
- Description: These scripts createn and call all views specifies for mmorpg database
****************************************************************/

USE MMORPG; #--specifying databbase that view must use
DROP VIEW IF EXISTS vwBlockedAccounts; #--Dropping and recreating view 
CREATE VIEW vwBlockedAccounts 
AS
 SELECT * FROM Accounts WHERE IsBlocked = 1; #--selecting all blocked accounts  with the pecific value 

SELECT * FROM vwBlockedAccounts;#-- showing results of view 




USE MMORPG;#--specifying databbase that view must use
DROP VIEW IF EXISTS vwTopSkill  ;#--Dropping and recreating view 
CREATE VIEW vwTopSkill AS
SELECT C.*, A.AccountName
FROM Characters C#--select characters and give it a allias 
JOIN Accounts A ON C.AccountID = A.AccountID#--joing data together  to make it more reading friendly 
ORDER BY SkillLevel DESC#--specefies the way the rows of data are ordered -decending 
LIMIT 20;#-- display limit 

Select * From vwTopSkill;#-- showing results of view 



USE mmorpg;#--specifying databbase that view must use
DROP  VIEW IF EXISTS vwTopStackedItems;#--Dropping and recreating view 
CREATE VIEW vwTopStackedItems AS
SELECT i.Name_s AS ItemName, COUNT(inv.ItemID) AS StackCount, GROUP_CONCAT(DISTINCT c.CharacterName ORDER BY c.CharacterName ASC) AS CharacterList
FROM Inventory inv
JOIN Items i ON i.ItemID = inv.ItemID# joining on related PK/FK between tables
JOIN Characters c ON c.CharacterID = inv.CharacterID# joining on related PK/FK between tables
# When using an aggregate function within a select statement like SUM, the columns in the select statement
# that does not have an aggregate function must be included in a GROUP BY clause
GROUP BY i.Name_s
ORDER BY StackCount DESC
LIMIT 20;#limimt the number of outputs we recieve 

SELECT * FROM vwTopStackedItems;#-- showing results of view 






USE mmorpg;#--specifying databbase that view must use

DROP VIEW IF EXISTS vwPopItems;#--Dropping and recreating view 
CREATE VIEW vwPopItems 
AS
 SELECT i.Name_s AS ItemName, COUNT(DISTINCT inv.CharacterID) AS CharacterCount
 FROM Items i
 JOIN Inventory inv ON i.ItemID = inv.ItemID# joining on related PK/FK between tables
 GROUP BY i.Name_s
 ORDER BY CharacterCount DESC # determining the orer the rows are returned in 
 LIMIT 5; # set limit of how many rows to return 

select *  from vwPopItems;#-- showing results of view 