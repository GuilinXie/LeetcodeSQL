# Write your MySQL query statement below

SELECT t.Request_at AS Day, ROUND(SUM(cancel) / SUM(total), 2) AS "Cancellation Rate"

FROM
(SELECT t1.Request_at,
 CASE WHEN t1.Status="cancelled_by_driver" THEN 1 WHEN t1.status="cancelled_by_client" THEN 1 ELSE 0 END AS cancel,
 1 AS total

 FROM Trips t1

 WHERE t1.Client_Id IN
 (SELECT DISTINCT Users_Id
 FROM Users u
 WHERE u.Banned="No")

AND
t1.Driver_Id IN
(SELECT DISTINCT Users_Id
FROM Users u
WHERE u.Banned = "No")

AND t1.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
) t
GROUP BY t.Request_at
