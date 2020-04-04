# Method 1 - beat 80%
# UNION NULL directly to get NULL
SELECT DISTINCT(Salary) AS SecondHighestSalary
FROM Employee
UNION
SELECT NULL
ORDER BY SecondHighestSalary DESC
LIMIT 1,1

# Method2 - beat 50%, sometimes beat 90%...
# max() will return NULL, if not exist
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)