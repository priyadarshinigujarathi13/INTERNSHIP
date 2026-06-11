
USE internship_db;

CREATE TABLE Employee04(
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

INSERT INTO Employee04 VALUES
(1,'Darshini','IT',50000),
(2,'Ravi','HR',40000),
(3,'Kiran','IT',60000);

SELECT * FROM Employee04;