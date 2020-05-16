# Write your MySQL query statement below

SELECT IFNULL(ROUND(SUM(sessions) / COUNT(user_id), 2), 0.00) AS average_sessions_per_user
FROM
(SELECT user_id, COUNT(DISTINCT session_id) AS sessions
FROM Activity
WHERE DATEDIFF("2019-07-27", activity_date) < 30
GROUP BY user_id) t