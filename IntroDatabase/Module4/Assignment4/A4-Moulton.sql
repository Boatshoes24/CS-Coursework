/***************************/
/* Name: Wade Moulton */
/* Class: CS3410 */
/* Term: Fall 2018 */
/* Assgn #: 4 */
/***************************/

/* A */
SELECT *
FROM PROJECT;

/* B */
SELECT ProjectID, Name, StartDate, EndDate
FROM PROJECT;

/* C */
SELECT *
FROM PROJECT
WHERE StartDate < '2008-08-01';

/* D */
SELECT *
FROM PROJECT
WHERE EndDate IS NULL;

/* E */
SELECT P.ProjectID, E.EmployeeNumber, E.LastName, E.FirstName, E.Phone
FROM PROJECT P
LEFT JOIN EMPLOYEE E ON P.Department = E.Department;

/* F */
SELECT P.ProjectID, P.Name, P.Department, E.EmployeeNumber, E.LastName, E.FirstName, E.Phone
FROM PROJECT P
LEFT JOIN EMPLOYEE E ON P.Department = E.Department;

/* G */
SELECT P.ProjectID, P.Name, P.Department, D.Phone, E.EmployeeNumber, E.LastName, E.FirstName, E.Phone
FROM PROJECT P
LEFT JOIN EMPLOYEE E ON P.Department = E.Department
LEFT JOIN DEPARTMENT D ON P.Department = D.DepartmentName
ORDER BY P.ProjectID;

/* H */
SELECT P.ProjectID, P.Name, P.Department, D.Phone, E.EmployeeNumber, E.LastName, E.FirstName, E.Phone
FROM PROJECT P
LEFT JOIN EMPLOYEE E ON P.Department = E.Department
LEFT JOIN DEPARTMENT D ON P.Department = D.DepartmentName
WHERE P.Department = 'Marketing'
ORDER BY ProjectID;  

/* I */
SELECT COUNT(*) AS NumberOfMarketingProjects
FROM PROJECT
WHERE Department = 'Marketing';

/* J */
SELECT SUM(MaxHours) AS MarketingTotalMaxHours
FROM PROJECT 
WHERE Department = 'Marketing';

/* K */
SELECT AVG(MaxHours) AS MarketingAverageMaxHours
FROM PROJECT 
WHERE Department = 'Marketing';

/* L */
SELECT Department, COUNT(*) AS NumberOfProjects
FROM PROJECT
GROUP BY Department;
