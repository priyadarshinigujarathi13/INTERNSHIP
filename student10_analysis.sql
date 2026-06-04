CREATE DATABASE college;
USE college;

CREATE TABLE student10(
    id INT,
    name VARCHAR(50),
    marks INT
);

INSERT INTO student10 VALUES
(1,'Ravi',60000),
(2,'Priya',70000),
(3,'Ram',80000);

SELECT * FROM student10;

SELECT COUNT(*) AS total_students
FROM student10;

SELECT AVG(marks) AS avg_marks
FROM student10;

SELECT MAX(marks) AS highest_marks,
       MIN(marks) AS lowest_marks
FROM student10;

SELECT SUM(marks) AS total_marks
FROM student10;