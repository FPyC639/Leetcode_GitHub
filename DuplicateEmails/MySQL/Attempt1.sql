Select B.em As Email From 
(Select email AS em, COUNT(email) AS ct From Person GROUP BY em) AS B
Where B.ct >= 2;