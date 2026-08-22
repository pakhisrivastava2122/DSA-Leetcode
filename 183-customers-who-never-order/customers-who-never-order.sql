-- # Write your MySQL query statement below
-- SELECT name from Customers where id <> (SELECT customerId from Orders);

SELECT name as Customers FROM Customers C left join Orders o on o.customerId = C.id where o.customerId is null ;