USE internship_db;

CREATE TABLE Department02(
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

INSERT INTO Department02 VALUES
(1,'IT'),
(2,'HR'),
(3,'Finance');

CREATE TABLE Employee05(
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    Salary INT
);

INSERT INTO Employee05 VALUES
(1,'Darshini',1,50000),
(2,'Ravi',2,40000),
(3,'Kiran',1,60000);

SELECT e.EmpName,
       d.DeptName,
       e.Salary
FROM Employee05 e
INNER JOIN Department02 d
ON e.DeptID = d.DeptID;