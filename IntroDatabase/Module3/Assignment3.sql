/***************************/
/* Name: Wade Moulton */
/* Class: CS3410 */
/* Term: Fall 2018 */
/* Assgn #: 3 */
/***************************/

USE Cape_Codd;

/* 2.28 */
SELECT SKU, SKU_Description, WarehouseID
FROM INVENTORY
WHERE (QuantityOnHand = 0) OR (QuantityOnOrder = 0)
ORDER BY WarehouseID DESC, SKU;

/* 2.29 */
SELECT SKU, SKU_Description, WarehouseID, QuantityOnHand
FROM INVENTORY
WHERE (QuantityOnHand > 1) AND (QuantityOnHand < 10);

/* 2.30 */
SELECT SKU, SKU_Description, WarehouseID, QuantityOnHand
FROM INVENTORY
WHERE QuantityOnHand BETWEEN 2 AND 9;

/* 2.31 */
SELECT DISTINCT SKU, SKU_Description
FROM INVENTORY
WHERE SKU_Description LIKE 'Half-dome%';

/* 2.32 */
SELECT DISTINCT SKU, SKU_Description
FROM INVENTORY
WHERE SKU_Description LIKE '%Climb%';

/* 2.33 */
SELECT DISTINCT SKU, SKU_Description
FROM INVENTORY
WHERE SKU_Description LIKE '__d%';

/* 2.34 */
SELECT COUNT(QuantityOnHand) AS NumRows,
	   SUM(QuantityOnHand) AS TotalQuantityOnHand,
	   MAX(QuantityOnHand) AS HighestQuantityOnHand,
	   MIN(QuantityOnHand) AS LowestQuantityOnHand,
	   AVG(QuantityOnHand) AS AverageQuantityOnHand
FROM INVENTORY;

/* 2.35 */
/* COUNT returns the number of rows matching the given criteria while */ 
/* SUM returns the total of all values in the given column. */

/* 2.36 */
SELECT WarehouseID, SUM(QuantityOnHand) AS TotalItemsOnHand
FROM INVENTORY
GROUP BY WarehouseID
ORDER BY TotalItemsOnHand DESC;

/* 2.37 */
SELECT WarehouseID, SUM(QuantityOnHand) AS TotalItemsOnHandLT3
FROM INVENTORY
WHERE QuantityOnHand < 3
GROUP BY WarehouseID
ORDER BY TotalItemsOnHandLT3 DESC;

/* 2.38 */
SELECT WarehouseID, SUM(QuantityOnHand) AS TotalItemsOnHandLT3
FROM INVENTORY
WHERE QuantityOnHand < 3
GROUP BY WarehouseID 
HAVING COUNT(*) < 2
ORDER BY TotalItemsOnHandLT3 DESC;

/* 2.39 */
/* The WHERE clause is applied first or else there would be different results based on which was applied first. */

/* 2.40 */
SELECT SKU, SKU_Description, WAREHOUSE.WarehouseID, WarehouseCity, WarehouseState
FROM INVENTORY, WAREHOUSE
WHERE INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
AND (WarehouseCity = 'Atlanta' OR WarehouseCity = 'Bangor' OR WarehouseCity = 'Chicago');

/* 2.41 */
SELECT SKU, SKU_Description, WAREHOUSE.WarehouseID, WarehouseCity, WarehouseState
FROM INVENTORY, WAREHOUSE
WHERE INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
AND WarehouseCity IN ('Atlanta', 'Bangor', 'Chicago');

/* 2.42 */
SELECT SKU, SKU_Description, WAREHOUSE.WarehouseID, WarehouseCity, WarehouseState
FROM INVENTORY, WAREHOUSE
WHERE INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
AND (WarehouseCity <> 'Atlanta' AND WarehouseCity <> 'Bangor' AND WarehouseCity <> 'Chicago');

/* 2.43 */
SELECT SKU, SKU_Description, WAREHOUSE.WarehouseID, WarehouseCity, WarehouseState
FROM INVENTORY, WAREHOUSE
WHERE INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
AND WarehouseCity NOT IN ('Atlanta', 'Bangor', 'Chicago');

/* 2.44 */
SELECT SKU_Description+' is located in '+WarehouseCity AS ItemLocation
FROM INVENTORY, WAREHOUSE
WHERE INVENTORY.WarehouseID = WAREHOUSE.WarehouseID;

/* 2.45 */
SELECT SKU, SKU_Description, WarehouseID
FROM INVENTORY
WHERE WarehouseID IN
		(SELECT WarehouseID
		 FROM WAREHOUSE
		 WHERE Manager = 'Lucille Smith');

/* 2.46 */
SELECT SKU, SKU_Description, WAREHOUSE.WarehouseID
FROM INVENTORY, WAREHOUSE
WHERE INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
AND Manager = 'Lucille Smith';

/* 2.47 */
SELECT SKU, SKU_Description, WAREHOUSE.WarehouseID
FROM INVENTORY JOIN WAREHOUSE
ON INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
WHERE Manager = 'Lucille Smith';

/* 2.48 */
SELECT WarehouseID, AVG(QuantityOnHand) AS AverageQuantityOnHand
FROM INVENTORY
WHERE WarehouseID IN
		(SELECT WarehouseID
		 FROM WAREHOUSE
		 WHERE Manager = 'Lucille Smith')
GROUP BY WarehouseID;

/* 2.49 */
SELECT INVENTORY.WarehouseID, AVG(QuantityOnHand) AS AverageQuantityOnHand
FROM INVENTORY, WAREHOUSE
WHERE INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
AND Manager = 'Lucille Smith'
GROUP BY INVENTORY.WarehouseID;

/* 2.50 */
SELECT INVENTORY.WarehouseID, AVG(QuantityOnHand) AS AverageQuantityOnHand
FROM INVENTORY JOIN WAREHOUSE
ON INVENTORY.WarehouseID = WAREHOUSE.WarehouseID
WHERE Manager = 'Lucille Smith'
GROUP BY INVENTORY.WarehouseID;