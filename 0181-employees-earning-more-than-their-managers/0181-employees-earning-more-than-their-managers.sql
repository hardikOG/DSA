# Write your MySQL query statement below
SELECT m.name as Employee
FROM Employee e
INNER JOIN Employee m
ON e.id = m.managerId
WHERE e.salary<m.salary