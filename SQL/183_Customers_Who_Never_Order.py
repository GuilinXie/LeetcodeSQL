# Write your MySQL query statement below

# Method 1 - beat 98%
SELECT Name AS Customers
FROM Customers
WHERE Id not in
(SELECT DISTINCT CustomerId
FROM Orders)

# Method 2 - beat 36%
# Not use IS NULL, IS NOT NULL in WHERE clause,
# which is slow, as it can not use index when searching
SELECT c1.Name AS Customers
FROM Customers c1
LEFT JOIN
(SELECT DISTINCT CustomerId
FROM Orders) c2
ON c1.Id=c2.CustomerId
WHERE c2.CustomerId IS NULL