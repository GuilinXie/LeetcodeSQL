# Write your MySQL query statement below

# Method 1 -  use tmp table, beat 80%
SELECT e1.Name AS Employee
FROM Employee e1
JOIN
(SELECT Id, Salary
 FROM Employee) e2
ON e1.ManagerId = e2.Id
WHERE e1.Salary>e2.Salary


# Method 2 - Use entire table directly, beat 50%, slower
SELECT e1.Name AS Employee
FROM Employee e1, Employee e2
WHERE e1.ManagerId=e2.Id
AND e1.Salary>e2.Salary