SELECT
    `employee_id`,
    IF (`employee_id`%2 AND `name` NOT LIKE 'M%', `salary`, 0) 'bonus'
FROM `Employees`
ORDER BY `employee_id` ASC;

SELECT 
    `employee_id`,
    CASE
        WHEN `employee_id`%2 AND NOT `name` LIKE 'M%'
            THEN `salary`
            ELSE 0
    END AS `bonus`
FROM `Employees`
ORDER BY `employee_id` ASC;

SELECT 
    `employee_id`,
    CASE
        WHEN `employee_id`%2=0 OR `name` LIKE 'M%'
            THEN 0
            ELSE `salary`
    END AS `bonus`
FROM `Employees`
ORDER BY `employee_id` ASC;
