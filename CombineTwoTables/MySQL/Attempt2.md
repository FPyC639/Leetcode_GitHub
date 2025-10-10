**Time Complexity**

Assuming `n` rows in `Person` and `m` rows in `Address`:

- The `INNER JOIN` typically takes O(n * log m) if `Address.personID` is indexed, otherwise O(n * m).
- The `NOT EXISTS` subquery for each `Person` row checks for absence in `Address`, resulting in O(n * log m) with index, or O(n * m) without.
- The overall time complexity is **O(n * log m)** if indexed, otherwise **O(n * m)**.
- The `UNION ALL` operation is O(n), as it just concatenates results.

Indexes on `personID` in `Address` significantly improve performance.

```SQL
Select p.firstName, p.lastName, a.city, a.state 
FROM Person p
INNER JOIN Address a ON p.personID = a.personID

UNION ALL

Select firstName, lastName, NULL, NULL
FROM Person p
Where NOT EXISTS (SELECT 1 FROM Address a WHERE p.personID = a.personID)
```