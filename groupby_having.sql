SELECT Department,
       SUM(Salary) AS TotalSalary
FROM Employee04
GROUP BY Department;

SELECT Department,
       SUM(Salary) AS TotalSalary
FROM Employee04
GROUP BY Department
HAVING SUM(Salary) > 50000;