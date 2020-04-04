# Method 1 - beat 90% - select sub-table first before join
SELECT p.FirstName, p.LastName,t.City, t.State
FROM Person p
LEFT JOIN
(SELECT DISTINCT PersonId, City, State
FROM Address) t
ON t.PersonId=p.PersonId


# Method 2 - beat 50%
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person p
LEFT JOIN Address a
ON p.PersonId=a.PersonId