/***************************/
/* Name: Wade Moulton */
/* Class: CS3410 */
/* Term: Fall 2018 */
/* Lab #: 3part2 */
/***************************/
USE lab3
/* List the name of all products for which an order was placed. */
SELECT DISTINCT Pname
FROM products, orders
WHERE products.Pid = orders.Pid;

/* List the name of customers that ordered product 'p07' */
SELECT Cname
FROM customers
WHERE Cid IN
(SELECT Cid
FROM orders
WHERE Pid = 'p07');  

/* List name of agents that places an order for customer c003 or customer c006 */
SELECT Aname
FROM agents, orders
WHERE agents.Aid = orders.Aid AND orders.Cid = 'c003' or orders.Cid = 'c006';

/* List name of customers that ordered product 'p01' through agent 'a01' */
SELECT Cname
FROM customers, orders
WHERE (customers.CId = orders.Cid) AND (orders.Pid = 'p01') AND (orders.Aid = 'a01');

/* List the name of each customer that placed an order, the pid what they ordered. */
SELECT Cname, Pid
FROM customers, orders
WHERE customers.Cid = orders.Cid;

/* List the name of each customer that placed an order and the product name for each product they ordered. */
SELECT Cname, Pname
FROM customers, orders, products
WHERE (customers.Cid = orders.Cid) AND (orders.Pid = products.Pid);

/* List the name of each customer and the total amount ordered by the customer. */
SELECT Cname, SUM(orders.Qty) AS TotalOrders
FROM customers, orders
WHERE customers.Cid = orders.Cid
GROUP BY customers.CName;

/* List the name and the sum of dollars for each customer that ordered more than $1,000 */
SELECT Cname, SUM(orders.Dollars) AS TotalDollars
FROM customers, orders
WHERE customers.Cid = orders.Cid
GROUP BY customers.Cname
HAVING SUM(orders.Dollars) > 1000; 

/* List the agent name, product name and customer name for each product ordered */
SELECT Aname, Pname, Cname
FROM orders 
INNER JOIN agents
ON agents.Aid = orders.Aid
INNER JOIN products
ON products.Pid = orders.Pid
INNER JOIN customers
ON customers.CId = orders.Cid;

/***********************************************************/
/* What would be the result of the following SQL Statement */
/*             SELECT * FROM CUSTOMERS, PRODUCTS           */
/*    This statement would return all content from the     */ 
/*             customers and products tables               */
/***********************************************************/