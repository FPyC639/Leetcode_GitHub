Select p.firstName, p.lastName, a.city, a.state 
FROM Person p
INNER JOIN Address a ON p.personID = a.personID

UNION ALL

Select firstName, lastName, NULL, NULL
FROM Person p
Where NOT EXISTS (SELECT 1 FROM Address a WHERE p.personID = a.personID)