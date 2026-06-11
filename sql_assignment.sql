CREATE DATABASE internship_db;
USE internship_db;

CREATE TABLE Employee(
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

INSERT INTO Employee VALUES
(1,'Darshini','IT',50000),
(2,'Ravi','HR',40000),
(3,'Kiran','IT',60000);

SELECT * FROM Employee;

SELECT Department,
       SUM(Salary) AS TotalSalary
FROM Employee
GROUP BY Department;

SELECT Department,
       SUM(Salary) AS TotalSalary
FROM Employee
GROUP BY Department
HAVING SUM(Salary) > 50000;

CREATE TABLE Department(
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

INSERT INTO Department VALUES
(1,'IT'),
(2,'HR'),
(3,'Finance');

CREATE TABLE Employee2(
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    Salary INT
);

INSERT INTO Employee2 VALUES
(1,'Darshini',1,50000),
(2,'Ravi',2,40000),
(3,'Kiran',1,60000);

SELECT e.EmpName,
       d.DeptName,
       e.Salary
FROM Employee2 e
INNER JOIN Department d
ON e.DeptID = d.DeptID;