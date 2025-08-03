/* Write your T-SQL query statement below */

SELECT
    name,
    bonus
FROM (
    SELECT
        E.empId,
        E.name,
        B.bonus
    FROM
        Employee E
        LEFT JOIN Bonus B ON B.empId = E.empId 
    WHERE
        B.bonus < 1000
    UNION ALL
    SELECT
        E.empId,
        E.name,
        B.bonus
    FROM
        Employee E
        LEFT JOIN Bonus B ON B.empId = E.empId 
    WHERE
        B.bonus IS NULL
) TB;