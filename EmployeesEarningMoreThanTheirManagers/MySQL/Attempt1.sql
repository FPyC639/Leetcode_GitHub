# Write your MySQL query statement below
Select B.name AS Employee From 
(SELECT Q.name, W.salary AS C, Q.salary AS D from Employee W INNER JOIN Employee Q Where W.id = Q.managerID ) AS B
Where C < D;