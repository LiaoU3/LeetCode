SELECT d.`name` 'Department', e.`name` 'Employee', max(e.`salary`) 'Salary'
FROM `Employee` e LEFT JOIN `Department` d
ON e.`departmentID`=d.`id`
GROUP BY e.`departmentID`;
