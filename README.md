### LeetcodeSQL

According to frequency

| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge   |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- |
| 176   | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/176_Sencond_Highest_Salary.py) | Easy     |  if not exist, return NULL  |
| 175   | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/175_Combine_Two_Tables.py) | Easy     |  select sub-table before join  |
| 177   | [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/177_Nth_Highest_Salary.py) | Medium     |  CREATE FUNCTION, SET, MAX COUNT , LIMIT N,1 equals to LIMIT 1 OFFSET N |
| 262   | [Trips and Users](https://leetcode.com/problems/trips-and-users/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/262_Trips_and_Users.py) | Hard     |  CASE WHEN at inner loop, then SUM GROUP BY, ROUND, new name "Cancellation Rate" with a space, t.Request_at BETWEEN '2013-10-01' AND '2013-10-03' includes [2013-10-01, 2013-10-03] |
| 181   | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/181_Employees_Earning_More_Than_Their_Managers.py) | Easy     |  tmp_table is faster than using entire table  |
| 178   | [Rank Scores](https://leetcode.com/problems/rank-scores/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/178_Rank_Scores.py) | Medium     |  Rank consecutively, what if not consecutively, what if same score rank differently?  |
| 1179  | [Reformat Department Table](https://leetcode.com/problems/reformat-department-table/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/1179_Reformat_Department_Table.py) | Easy     |  CASE WHEN change column to differnt rows  |
| 180  | [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/180_Consecutive_Numbers.py) | Medium     |  Consecutive implement  |
| 1212  | [Team Scores in Football Tournament](https://leetcode.com/problems/team-scores-in-football-tournament/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/1212_Team_Scores_in_Football_Tournament.py) | Medium     |  IFNULL(name, 0), SUM() can not be in IFNULL function, UNION ALL  |
| 185  | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/185_Department_Top_Three_Salaries.py) | Hard     |  Top3 for different departments, window function: DENSE_RANK(PARTITION BY * ORDER BY * DESC) AS rk...WHERE rk <= 3 |
| 184  | [Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/184_Department_Highest_Salary.py) | Medium     |  Can use same method as 185, or use (MAX(Salary), DepartmentId) to check the highest  |
| 183  | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/183_Customers_Who_Never_Order.py) | Easy     | Not use IS NULL, IS NOT NULL in WEHRE clause, which can be slower |
| 1241  | [Number of Comments per Post](https://leetcode.com/problems/number-of-comments-per-post/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/1241_Number_of_Comments_per_Post.py) | Easy     | has to use IS NULL, IS NOT NULL in this case, IFNULL(cnt, 0) |
| 1270  | [All People Report to the Given Manager](https://leetcode.com/problems/all-people-report-to-the-given-manager/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/1270_All_People_Report_to_the_Given_Manager.py) | Medium | chain join and join...  |
| 618  | [Students Report By Geography](https://leetcode.com/problems/students-report-by-geography/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/618_Students_Report_By_Geography.py) | Hard | Why need those MAX ??  |
| 597  | [Friend Requests 1: Overall Acceptance Rate](https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/597_Friend_Requests_1_Overall_Acceptance_Rate.py) | Easy | IFNULL() |
| 1341  | [Movie Rating](https://leetcode.com/problems/movie-rating/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/1341_Movie_Rating.py) | Medium | created_at="2020-02-15" to get Februrary substring(created_at,1,7)="2020-02", UNION, AVG=SUM/COUNT, ORDER BY..DESC, LIMIT 1 |
| 1142  | [User Activity for the Past 30 Days 2](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/1142_User_Activity_for_the_Past_30_Days_2.py) | Easy | IFNULL, ROUND, DITEDIFF(biggerDate, smallerDate)<30 |
| 577  | [Employee Bonus](https://leetcode.com/problems/employee-bonus/) | [SQL](https://github.com/GuilinXie/LeetcodeSQL/blob/master/SQL/577_employee_bonus.py) | Easy | Do not forget NULL |


### Optimization Idea:
1. Only select those columns that needed, when joining two tables, can first select sub-table for necessary columns. Eg. 175

### Question:
1. How to deal with date, Unix timestamps   
  **created_at = "2020-02-13"**   
  **substring(created_at, 1, 7)="2020-02"**  -> to get Februray data, but **substring(created_at,6,7)="02" does not get correct "02"**,      need more information about this...   
  **Reason**: substring(created_at, 6, 2)="02" should be the correct solution, as the 2 refers to the number of chars starting from position 6. BTW, the first char's index starting from 1, not 0.
  
 Reference:
 1. Leetcode
 2. SQL, create, read, update, delete:
     https://blog.csdn.net/woaidapaopao/article/details/78030449
 
