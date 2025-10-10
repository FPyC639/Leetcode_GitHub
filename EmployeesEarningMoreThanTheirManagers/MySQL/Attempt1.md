### 🧠 Query Explanation

- **Purpose:**  
  Retrieves the names of employees whose salary is **less than their manager's salary**.

- **How It Works:**  
  The query performs a **self-join** on the `Employee` table to pair each employee with their corresponding manager,  
  then filters the results to include only those employees whose salary is **lower** than their manager's.

- **Time Complexity:**  
  `$O(N^2)$` — where `N` is the number of employees, due to the **self-join** operation that compares each employee–manager pair.

```SQL
# Write your MySQL query statement below
Select B.name AS Employee From 
(SELECT Q.name, W.salary AS C, Q.salary AS D from Employee W INNER JOIN Employee Q Where W.id = Q.managerID ) AS B
Where C < D;
```