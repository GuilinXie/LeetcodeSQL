# Solution 1 - beat 65%
select
e1.employee_id
from employees e1
join employees e2 on e1.manager_id = e2.employee_id
join employees e3 on e2.manager_id = e3.employee_id
where e3.manager_id = 1 and e1.employee_id != 1


# Solution 2 - beat 15%
select
t.employee_id
from (
select
e1.employee_id,
e2.manager_id as direct_manager,
e3.manager_id as indirect_manager
from employees e1
left join employees e2 on e1.manager_id = e2.employee_id
left join employees e3 on e2.manager_id = e3.employee_id
#order by e1.employee_id
)t
where t.indirect_manager = 1 and t.employee_id != 1
ORDER BY t.employee_id