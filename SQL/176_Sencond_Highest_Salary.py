# Method 1 - beat 80%
# UNION NULL directly to get NULL
SELECT DISTINCT(Salary) AS SecondHighestSalary
FROM Employee
UNION
SELECT NULL
ORDER BY SecondHighestSalary DESC
LIMIT 1,1

# Method 2 - RANK() window function - beat 10%, slower but suitable for Nth salary
# Use MAX to return null if not exits.
SELECT MAX(Salary) AS SecondHighestSalary
FROM (
    SELECT Salary, RANK() OVER (ORDER BY Salary DESC) RN
    FROM Employee
) A
WHERE RN = 2


# Method3 - beat 50%, sometimes beat 90%..., but not suitable for Nth salary
# max() will return NULL, if not exist
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
