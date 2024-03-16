/***************************************************************

- Author: Joshua singrew
- Date: 23 october 2023
- Filename: spAddChar .sql
- Description: This script adds character to specific  account
****************************************************************/


USE MMORPG;

DELIMITER $$

DROP PROCEDURE IF EXISTS MMORPG.spAddChar $$

CREATE PROCEDURE  MMORPG.spAddChar (IN  account_Name_var VARCHAR(50),IN character_name_var VARCHAR(50),IN character_Team_var VARCHAR(50), IN character_Skill_var INT )

BEGIN
INSERT INTO characters (AccountID,CharacterName, Team , SkillLevel)#insert data into vlaues 
VALUES (account_Name_var, character_name_var, character_Team_var,character_Skill_var);

END$$

DELIMITER ;

call spAddChar ('2','geno','TEAM 3','6');#--testing spAddChar 

SELECT * FROM characters;