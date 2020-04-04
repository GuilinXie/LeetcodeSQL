# Method 1 - beat 45%
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
  SELECT DISTINCT(Salary)
  FROM Employee
# GROUP BY can be faster than DISTINCT
#  GROUP BY Salary
  ORDER BY Salary DESC LIMIT N,1
);
END

# Method 2 - beat 10%
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
select DISTINCT e1.salary
FROM Employee e1
WHERE N-1 = (SELECT COUNT(DISTINCT e2.Salary) FROM Employee e2 WHERE e1.Salary < e2.Salary)
);
END
