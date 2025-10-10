**Time Complexity Analysis**

- Without index on `Address.personID`: $O(n \times m)$
- With index on `Address.personID`: $O(n \log m)$ (or better, depending on the database engine)

```SQL
Select firstName, lastName, city, state
From Person 
Left Join Address
ON Person.personId = Address.personID;
```
