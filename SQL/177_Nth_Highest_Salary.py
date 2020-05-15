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

# Method 2 - beat 20% - DENSE_RANK(), suitable for Nth, need to clarify if it is a DENSE_RANK() or a RANK()
# DENSE_RANK(), 1,1,2,3,3,4...
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT MAX(Salary)
      FROM
      (SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS rk
       FROM Employee
      ) e
      WHERE rk=N
  );
END

# Method 3 - beat 10%
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
select DISTINCT e1.salary
FROM Employee e1
WHERE N-1 = (SELECT COUNT(DISTINCT e2.Salary) FROM Employee e2 WHERE e1.Salary < e2.Salary)
);
END
