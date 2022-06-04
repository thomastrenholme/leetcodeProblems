/* Write your T-SQL query statement below */


Select e.name as Employee from Employee e where e.salary > (select m.salary from Employee m where m.id = e.managerId)



/*https://leetcode.com/problems/employees-earning-more-than-their-managers/ */