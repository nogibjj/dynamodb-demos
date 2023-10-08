-- Active: 1696708919577@@127.0.0.1@3306

#CREATE DATABASE School_Attendance;

show tables;

DEFAULT CHARACTER SET = 'utf8mb4';

USE School_Attendance;

CREATE TABLE
    School_Attendance_Table (
        District_code VARCHAR(255),
        District_name VARCHAR(255),
        Category VARCHAR(255),
        Student_group VARCHAR(255),
        `2021-2022_student_count_-_year_to_date` INT,
        `2021-2022_attendance_rate_-_year_to_date` FLOAT,
        `2020-2021_student_count` INT,
        `2020-2021_attendance_rate` FLOAT,
        `2019-2020_student_count` INT,
        `2019-2020_attendance_rate` FLOAT,
        Reporting_period DATE,
        Date_update DATE
    );

SET GLOBAL local_infile=1;

show tables;

LOAD DATA
    LOCAL INFILE '/Users/castnut/Desktop/706_Data_Engineering/mini_6/Jiechen_Li_Mini_6_External_Database/School_Attendance_by_Student_Group_and_District__2021-2022.csv' INTO
TABLE
    School_Attendance_Table FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

-- This is to ignore the header row in the CSV

SELECT * FROM School_Attendance_Table LIMIT 10;

#Query 1: Calculate the average attendance rate across all districts for 2021-2022.

#SELECT AVG(`2021-2022_attendance_rate_-_year_to_date`) AS average_attendance_rate_2021_2022

#FROM School_Attendance_Table;

-- Creating the attendance_2021_2022 table

CREATE TABLE
    attendance_2021_2022 (
        District_code VARCHAR(255),
        District_name VARCHAR(255),
        Category VARCHAR(255),
        Student_group VARCHAR(255),
        Student_count INT,
        Attendance_rate FLOAT
    );

-- Inserting data into the attendance_2021_2022 table

INSERT INTO
    attendance_2021_2022 (
        District_code,
        District_name,
        Category,
        Student_group,
        Student_count,
        Attendance_rate
    )
SELECT
    District_code,
    District_name,
    Category,
    student_group,
    `2021-2022_student_count_-_year_to_date`,
    `2021-2022_attendance_rate_-_year_to_date`
FROM
    `School_Attendance_Table`;

-- Creating the attendance_2020_2021 table

CREATE TABLE
    attendance_2020_2021 (
        District_code VARCHAR(255),
        District_name VARCHAR(255),
        Category VARCHAR(255),
        Student_group VARCHAR(255),
        Student_count INT,
        Attendance_rate FLOAT
    );

-- Inserting data into the attendance_2020_2021 table

INSERT INTO
    attendance_2020_2021 (
        District_code,
        District_name,
        Category,
        Student_group,
        Student_count,
        Attendance_rate
    )
SELECT
    District_code,
    District_name,
    Category,
    student_group,
    `2020-2021_student_count`,
    `2020-2021_attendance_rate`
FROM
    `School_Attendance_Table`;

WITH Comparison AS (
        SELECT
            a21.District_code,
            a21.District_name,
            a21.Attendance_rate AS rate_2021_2022,
            a20.Attendance_rate AS rate_2020_2021, (
                a21.Attendance_rate - a20.Attendance_rate
            ) AS rate_difference
        FROM
            attendance_2021_2022 AS a21
            JOIN attendance_2020_2021 AS a20 ON a21.District_code = a20.District_code
        WHERE
            a21.Student_group = 'All Students'
            AND a20.Student_group = 'All Students'
    )
SELECT
    District_code,
    District_name,
    CASE
        WHEN rate_difference > 0.01 THEN 'Increased'
        WHEN rate_difference BETWEEN -0.01 AND 0.01 THEN 'Stable'
        ELSE 'Decreased'
    END AS Attendance_trend,
    rate_2021_2022,
    rate_2020_2021
FROM Comparison
ORDER BY rate_difference DESC;