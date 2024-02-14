-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- in your MySQL server. You need to convert all of the following to UTF8:


-- Database hbtn_0c_0
USE hbtn_0c_0 ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ALTER DATABASE hbtn_0c_0 IF EXISTS CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- -- Table first_table
-- ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- -- Field name in first_table
-- ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
