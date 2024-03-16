/***************************************************************

- Author: Joshua singrew
- Date: 23 october 2023
- Filename: Inserting .sql
- Description: This script Inserts data into the databse tables
****************************************************************/

INSERT   INTO Person(PersonName,PersonEmail)
VALUES('Megan','megan@gmail.com'),
('felani','fefe@gmail.com'),
('Alexxi','Alexxa@outlook.com'),
('OOPALU','OOpies@gmail.com'),
('Vusi','vusi @gmail.com'),
('Aimy','Q@gmail.com'),
('Toney' ,'Topman@gmail.com'),
('Amoora','amooer@gmail.com'),
('yaka','yaka@gmail.com'),
('mooza','lakaaka@gmail.com');
#--data gettin inserted into the accounts table
INSERT IGNORE  INTO Accounts(AccountID , AccountName , ExpiryDate ,IsBlocked,PersonEmail )
VALUES
('1','HEETHER',CURDATE(),'0','megan@gmail.com'),
('2','MARLOW',CURDATE() + 1,'0','fefe@gmail.com'),
('3','POOHOO',CURDATE() - 10,'1','Alexxa@outlook.com'),
('4','REAPER23',CURDATE() + 50,'0','OOpies@gmail.com'),
('5','JACK-HOU',CURDATE() -100,'1','vusi @gmail.com'),
('6','SINDEY ARLOW',CURDATE() + 8,'0','Q@gmail.com'),
('7','KITH',CURDATE() + 2,'0','Topman@gmail.com'),
('8','NAI',CURDATE() -9,'0','amooer@gmail.com');
#--data gets inserteed into character table
INSERT INTO Characters(CharacterName, Team,AccountID,
SkillLevel  )
VALUES('MOOGLA','TEAM-1','1','55'),
('amazoinia','TEAM-1','1','4'),
('batman','TEAM-2','2','100'),
('zues','TEAM-2','3','20'),
('zoolander','TEAM-1','4','1'),
('Adem sandler','TEAM-2','5','99'),
('geko','TEAM-3','6','40'),
('penguin','TEAM-2','7','69'),
('gamboy01','TEAM-1','8',70),
('kraytos','TEAM-3','6','34'),
('man','TEAM-3','4','20'),
('MA','TEAM-3','3','60'),
('MAleos','TEAM-1','3','60'),
('leam','TEAM-2','3','33'),
('vook','TEAM-4','3','34'),
('n','TEAM-1','3','86'),
('zalos','TEAM-3','3','67'),
('kye','TEAM-2','3','70'),
('masoola','TEAM-3','3','0'),
('hydro','TEAM-4','3','0'),
('MAgatu','TEAM-4','3','99'),
('MAzoola','TEAM-1','3','3');
#--data gets inserted into item table
INSERT INTO  items(Name_s,Description)
VALUES ('zulu1','short-SWORD'),
('samurai sword','Longs-SWORD'),
('Hellcat 9mm','Gun-Pistol'),
('AK47','Gun-Rifle'),
('m2409 rifle','Gun-Heavy-Machine-gun'),
('lo1','bow-Lonbow'),
('wash yourself','sanitary-soap'),
('Poisoned water','Nacecity-Water'),
('Hide','Nacecity-Raw Meate'),
('Expired meate','Nacecity-Cooked Meate'),
('BOOM-Pow',' stunn-Grenade '),
('BOOM-BOOM','shrapnell-Grenade'),
('Mony','TOKEN-Gold'),
('Map of quala','Map'),
('beanco expired beans ','Can-Beans'),
('lance','Short-spear'),
('Coat of bear ','Animal-fur');
#--data gets inserted into the  inventory table
INSERT INTO Inventory(CharacterID ,ItemID ,Quantity )
VALUES('1','17','7'),
('1','4','100'),
('1','8','1'),
('1','7','2'),
('1','3','55'),
('1','2','5'),
('1','1','1'),
('1','9','2'),
('2','2','60'),
('3','5','6'),
('5','7','23'),
('2','6','22'),
('6','3','3'),
('2','2','1'),
('9','8','8');