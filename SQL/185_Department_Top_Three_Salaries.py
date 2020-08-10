# Write your MySQL query statement below

# Solution 0 - window function - easier to understand
# beat 61%
SELECT t.Department, t.Employee, t.Salary
FROM 
(SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary, DENSE_RANK() OVER(PARTITION BY e.DepartmentId ORDER BY e.Salary DESC) AS rk
FROM Employee e
INNER JOIN Department d   # inner join means if the departmentId is not find, then drop this rows, if use LEFT JOIN, then will keep it with DepartmentId and DepartmentName as NULL
ON e.DepartmentId=d.Id) t
WHERE t.rk <= 3


# Solution 1 - Record my own, beat 98%
SELECT d.Name AS Department, e1.Name AS Employee, e1.Salary
FROM Employee e1
JOIN Department d ON e1.DepartmentId = d.Id

WHERE 3 >= (SELECT COUNT(e2.Salary) FROM
      (SELECT DISTINCT DepartmentId, Salary FROM Employee) e2
       WHERE e1.Salary <= e2.Salary AND e2.DepartmentId = e1.DepartmentId
       )


# Solution 2 - from others
SELECT d.name AS Department, e1.Name AS Employee, e1.Salary
FROM Employee e1, Department d
WHERE e1.DepartmentId = d.Id
AND (SELECT COUNT(DISTINCT e2.Salary)
     FROM Employee e2
     WHERE e2.DepartmentId = e1.DepartmentId
     AND e2.Salary > e1.Salary
     ) < 3
