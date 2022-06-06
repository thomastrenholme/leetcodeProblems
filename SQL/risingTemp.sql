/* Write your T-SQL query statement below 
Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The query result format is in the following example.
*/


SELECT w1.id from Weather w1, Weather w2
WHERE w1.recordDate = DATEADD(day,1,w2.recordDate)
AND w1.temperature > w2.temperature