# Write your MySQL query statement below

# Method 0 - beat 50% - window function
SELECT t.Department, t.Employee, t.Salary
FROM
(
SELECT d.Name AS Department, e.Name AS Employee, e.Salary, RANK() OVER(PARTITION BY e.DepartmentId ORDER BY e.Salary DESC) AS rk
FROM Employee e
JOIN Department d
ON e.DepartmentId=d.Id
) t
WHERE rk=1


# Method 1 - beat 50%, similar to 185, Department top3
SELECT d.Name AS Department, e1.Name AS Employee, e1.Salary
FROM Employee e1
JOIN Department d
ON e1.DepartmentId=d.Id
WHERE 1=(SELECT COUNT(e2.Salary)
         FROM (SELECT DISTINCT DepartmentId, Salary FROM Employee) e2
         WHERE e1.DepartmentId=e2.DepartmentId AND e1.Salary<=e2.Salary
        )


# Method 2 - beat 98% - more direct using max for the highest
SELECT D.Name AS Department, E.Name AS Employee, E.Salary
FROM Employee E
INNER JOIN Department D
ON E.DepartmentId=D.Id
WHERE (Salary, DepartmentId) IN
(SELECT MAX(Salary) AS Salary, DepartmentId
FROM Employee
GROUP BY DepartmentId)
