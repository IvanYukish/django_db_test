-- select count of users by department name and id
-- using where and having
select department.name, count(worker.id)
from worker
         join department on department.id = worker.department_id
where worker.id != 2
GROUP BY department.name, department.id
having count(worker.id) > 6;

-- next
select department.id, avg(worker.salary)
from worker
         join department on department.id = worker.department_id
GROUP BY department.id
order by avg(worker.salary) desc
limit 3;
-- LIMIT 1
-- having count(worker.id) > 6


WITH DepartmentAvgSalaries AS (SELECT department.id, AVG(worker.salary) AS avg_salary
                               FROM worker
                                        join department on department.id = worker.department_id
                               GROUP BY department.id)

SELECT id, avg_salary
FROM DepartmentAvgSalaries
WHERE avg_salary = (SELECT max(avg_salary) FROM DepartmentAvgSalaries);
