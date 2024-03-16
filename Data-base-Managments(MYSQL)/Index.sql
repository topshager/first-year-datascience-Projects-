/***************************************************************

- Author: Joshua singrew
- Date: 23 october 2023
- Filename: Inserting .sql
- Description: Add index  to specific values to make them easier to find 
****************************************************************/
use mmorpg;
#DROP INDEX AccountName_index ON ACCOUNTS;#--drop index

CREATE  INDEX AccountName_index ON ACCOUNTS (AccountName);#--create index for accountName

CREATE  INDEX Person_Email_index on ACCOUNTS (PersonEmail);#--create index for person email