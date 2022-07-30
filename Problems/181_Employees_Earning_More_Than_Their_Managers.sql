SELECT a.`name` 'Employee'
FROM `Employee` a, `Employee` b
WHERE a.`managerId`=b.`id` AND a.`salary`>b.`salary`

SELECT a.`name` 'Employee'
FROM `Employee` a JOIN `Employee` b
ON a.`managerId`=b.`id` AND a.`Salary`>b.`salary`