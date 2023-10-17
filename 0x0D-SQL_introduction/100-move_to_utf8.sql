-- convert hbtn_0c_0 to UTF8 in MYsql
USE `hbtn_0c_0`
ALTER TABLE `firs_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
