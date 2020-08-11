# Write your MySQL query statement below

# How to use pivot table directly in mysql?

# Solution 1 - only beat 5%

SELECT t.id,
SUM(CASE WHEN month="Jan" THEN revenue ELSE NULL END) AS Jan_Revenue,
SUM(CASE WHEN month="Feb" THEN revenue ELSE NULL END) AS Feb_Revenue,
SUM(CASE WHEN month="Mar" THEN revenue ELSE NULL END) AS Mar_Revenue,
SUM(CASE WHEN month="Apr" THEN revenue ELSE NULL END) AS Apr_Revenue,
SUM(CASE WHEN month="May" THEN revenue ELSE NULL END) AS May_Revenue,
SUM(CASE WHEN month="Jun" THEN revenue ELSE NULL END) AS Jun_Revenue,
SUM(CASE WHEN month="Jul" THEN revenue ELSE NULL END) AS Jul_Revenue,
SUM(CASE WHEN month="Aug" THEN revenue ELSE NULL END) AS Aug_Revenue,
SUM(CASE WHEN month="Sep" THEN revenue ELSE NULL END) AS Sep_Revenue,
SUM(CASE WHEN month="Oct" THEN revenue ELSE NULL END) AS Oct_Revenue,
SUM(CASE WHEN month="Nov" THEN revenue ELSE NULL END) AS Nov_Revenue,
SUM(CASE WHEN month="Dec" THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department t
GROUP BY t.id


# Solution, similar to the previous one
SELECT t.id,
SUM(t.Jan_Revenue) AS Jan_Revenue,
SUM(t.Feb_Revenue) AS Feb_Revenue,
SUM(t.Mar_Revenue) AS Mar_Revenue,
SUM(t.Apr_Revenue) AS Apr_Revenue,
SUM(t.May_Revenue) AS May_Revenue,
SUM(t.Jun_Revenue) AS Jun_Revenue,
SUM(t.Jul_Revenue) AS Jul_Revenue,
SUM(t.Aug_Revenue) AS Aug_Revenue,
SUM(t.Sep_Revenue) AS Sep_Revenue,
SUM(t.Oct_Revenue) AS Oct_Revenue,
SUM(t.Nov_Revenue) AS Nov_Revenue,
SUM(t.Dec_Revenue) AS Dec_Revenue
FROM
(SELECT id,
CASE WHEN month="Jan" THEN revenue ELSE NULL END AS Jan_Revenue,
CASE WHEN month="Feb" THEN revenue ELSE NULL END AS Feb_Revenue,
CASE WHEN month="Mar" THEN revenue ELSE NULL END AS Mar_Revenue,
CASE WHEN month="Apr" THEN revenue ELSE NULL END AS Apr_Revenue,
CASE WHEN month="May" THEN revenue ELSE NULL END AS May_Revenue,
CASE WHEN month="Jun" THEN revenue ELSE NULL END AS Jun_Revenue,
CASE WHEN month="Jul" THEN revenue ELSE NULL END AS Jul_Revenue,
CASE WHEN month="Aug" THEN revenue ELSE NULL END AS Aug_Revenue,
CASE WHEN month="Sep" THEN revenue ELSE NULL END AS Sep_Revenue,
CASE WHEN month="Oct" THEN revenue ELSE NULL END AS Oct_Revenue,
CASE WHEN month="Nov" THEN revenue ELSE NULL END AS Nov_Revenue,
CASE WHEN month="Dec" THEN revenue ELSE NULL END AS Dec_Revenue
FROM Department) t
GROUP BY t.id
