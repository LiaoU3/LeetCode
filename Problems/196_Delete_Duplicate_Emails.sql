DELETE p1
FROM Person AS p1, Person AS p2
WHERE p1.Email=p2.Email AND p1.Id>p2.Id;

DELETE p1
FROM `Person` p1, `Person` p2
WHERE p1.`email`=p2.`email` AND p1.`id`>p2.`id`