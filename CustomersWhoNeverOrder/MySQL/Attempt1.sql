Select name AS Customers from Customers C
Where NOT EXISTS
(
    Select 1
    From Orders O
    Where C.id = O.customerId
);