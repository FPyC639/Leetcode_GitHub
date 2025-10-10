**Time Complexity Analysis**

- Without indexes: $O(n \times m)$
- With index on `Orders.customerId`: $O(n \log m)$

Where $n$ = number of customers, $m$ = number of orders.
```SQL
Select name AS Customers from Customers C
Where NOT EXISTS
(
    Select 1
    From Orders O
    Where C.id = O.customerId
);
```