-- I used MySQL
-- creats the Persons table
CREATE TABLE Persons (
    Person_id int,
    Personal_name varchar(255),
    Family_name varchar(255),
    Gender varchar(255),
    Father_id int,
	Mother_id int,
	Spouse_id int,	
    PRIMARY KEY (Person_id)
);
-- inserts people into the Persons table 2 and 3 spouses are null
INSERT INTO Persons (Person_id, Personal_name, Family_name, Gender, Father_id, Mother_id, Spouse_id) VALUES
(1, 'Abraham', 'Smith', 'Male', NULL, NULL, 2),
(2, 'Sarah', 'Smith', 'Female', NULL, NULL, NULL),
(3, 'Isaac', 'Smith', 'Male', 1, 2, NULL),
(4, 'Jacob', 'Smith', 'Male', 3, 6, 5),
(5, 'Rachel', 'Smith', 'Female', NULL, NULL, 4),
(6, 'Rivka', 'Smith', 'Female', NULL, NULL, 3),
(7, 'eisav', 'Smith', 'Male', 3, 6, NULL);

-- filling in missing spouses
UPDATE Persons p2
JOIN Persons p1 ON p1.Spouse_id = p2.Person_id
SET p2.Spouse_id = p1.Person_id
WHERE p2.Spouse_id IS NULL;



select * from Persons;

