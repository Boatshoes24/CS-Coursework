/***************************/
/* Name: Wade Moulton */
/* Class: CS 3410 */
/* Term: Fall 2018 */
/* Assgn #: 2 Part 1 */
/***************************/

USE Cape_Codd;

/* 2.17 */
SELECT SKU, SKU_Description
FROM INVENTORY;

/* 2.18 */
SELECT SKU_Description, SKU
FROM INVENTORY;

/* 2.19 */
SELECT WarehouseID
FROM INVENTORY;

/* 2.20 */
SELECT DISTINCT WarehouseID
FROM INVENTORY;

/* 2.21 */
SELECT WarehouseID, SKU, SKU_Description, QuantityOnHand, QuantityOnOrder
FROM INVENTORY;

/* 2.22 */
SELECT * 
FROM INVENTORY;

/* 2.23 */
SELECT * 
FROM INVENTORY
WHERE QuantityOnHand > 0;

/* 2.24 */
SELECT SKU, SKU_Description
FROM INVENTORY
WHERE QuantityOnHand = 0;

/* 2.25 */
SELECT SKU, SKU_Description, WarehouseID
FROM INVENTORY
WHERE QuantityOnHand = 0
ORDER BY WarehouseID;

/* 2.26 */
SELECT SKU, SKU_Description, WarehouseID
FROM INVENTORY
WHERE QuantityOnHand > 0
ORDER BY WarehouseID DESC, SKU; 

/* 2.27 */
SELECT SKU, SKU_Description, WarehouseID
FROM INVENTORY
WHERE QuantityOnHand = 0 AND QuantityOnOrder > 0
ORDER BY WarehouseID DESC, SKU;

/***************************/
/* Name: Wade Moulton */
/* Class: CS 3410 */
/* Term: Fall 2018 */
/* Assgn #: 2 Part 2 */
/***************************/

USE QACS;

/* A */
SELECT *
FROM CUSTOMER;

SELECT *
FROM ITEM;

SELECT *
FROM SALE;

SELECT *
FROM SALE_ITEM;

/* B */
SELECT LastName, FirstName, Phone
FROM CUSTOMER;

/* C */
SELECT LastName, FirstName, Phone
FROM CUSTOMER
WHERE FirstName = 'John';

/* D */
SELECT LastName, FirstName, Phone
FROM CUSTOMER
WHERE FirstName LIKE 'D%';

/* E */
SELECT LastName, FirstName, Phone
FROM CUSTOMER
WHERE LastName LIKE '%ne%';

/* F */
SELECT LastName, FirstName, Phone
FROM CUSTOMER
WHERE Phone LIKE '%56_';

/* G */
SELECT MAX(Total) AS MaxSalesTotal, MIN(Total) AS MinSalesTotal
FROM SALE;

/* H */
SELECT AVG(Total) AS AvgSalesTotal
FROM SALE;

/* I */ 
SELECT COUNT(*) AS NumCustomers
FROM CUSTOMER;

/* J */
SELECT LastName, FirstName
FROM CUSTOMER
GROUP BY LastName, FirstName;

/* K */
SELECT LastName, FirstName, COUNT(*) AS NumCustomers
FROM CUSTOMER
Group By LastName, FirstName;
