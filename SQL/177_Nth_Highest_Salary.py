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
from Employee e1
where N-1 = (select count(distinct e2.Salary) from Employee e2 where e1.Salary < e2.Salary)
);
END