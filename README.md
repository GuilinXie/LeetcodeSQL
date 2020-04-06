### LeetcodeSQL

According to frequency

| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge   |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- |
| 176   | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/176_Sencond_Highest_Salary.py) | Easy     |  if not exist, return NULL  |
| 175   | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/175_Combine_Two_Tables.py) | Easy     |  select sub-table before join  |
| 177   | [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/177_Nth_Highest_Salary.py) | Medium     |  CREATE FUNCTION, SET, MAX COUNT  |
| 262   | [Trips and Users](https://leetcode.com/problems/trips-and-users/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/262_Trips_and_Users.py) | Hard     |  CASE WHEN at inner loop, then SUM GROUP BY, ROUND, new name "Cancellation Rate" with a space  |


### Optimization Idea:
1. Only select those columns that needed, when joining two tables, can first select sub-table for necessary columns. Eg. 175
