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
-- inserts people into the Persons table
INSERT INTO Persons (Person_id, Personal_name, Family_name, Gender, Father_id, Mother_id, Spouse_id) VALUES
(1, 'Abraham', 'Smith', 'Male', NULL, NULL, 2),
(2, 'Sarah', 'Smith', 'Female', NULL, NULL, 1),
(3, 'Isaac', 'Smith', 'Male', 1, 2, 6),
(4, 'Jacob', 'Smith', 'Male', 3, 6, 5),
(5, 'Rachel', 'Smith', 'Female', NULL, NULL, 4),
(6, 'Rivka', 'Smith', 'Female', NULL, NULL, 3),
(7, 'eisav', 'Smith', 'Male', 3, 6, NULL);



-- creats the Conections table
CREATE TABLE Conections (
    Person_id int,
    Relative_id int,
    Connection_Type varchar(255),
    FOREIGN KEY (Person_id) REFERENCES Persons(Person_id),
    FOREIGN KEY (Relative_id) REFERENCES Persons(Person_id)
);
-- inserting into the Conections table
-- married
INSERT INTO Conections (Person_id, Relative_id, Connection_Type)
SELECT Person_id, Spouse_id, 'married'
FROM Persons
WHERE Spouse_id IS NOT NULL;

-- Father_id
INSERT INTO Conections (Person_id, Relative_id, Connection_Type)
SELECT Person_id, Father_id, 'father'
FROM Persons
WHERE Father_id IS NOT NULL;

-- Mother_id
INSERT INTO Conections (Person_id, Relative_id, Connection_Type)
SELECT Person_id, Mother_id, 'mother'
FROM Persons
WHERE Mother_id IS NOT NULL;

-- daughter
INSERT INTO Conections (Person_id, Relative_id, Connection_Type)
SELECT Mother_id, Person_id, 'daughter'
FROM Persons
WHERE Mother_id IS NOT NULL AND Gender = 'Female';

-- son
INSERT INTO Conections (Person_id, Relative_id, Connection_Type)
SELECT Father_id, Person_id, 'son'
FROM Persons
WHERE Father_id IS NOT NULL AND Gender = 'Male';

-- siblings
INSERT INTO Conections (Person_id, Relative_id, Connection_Type)
SELECT p1.Person_id, p2.Person_id, 'Siblings'
FROM Persons p1
JOIN Persons p2
    ON p1.Father_id = p2.Father_id
   AND p1.Mother_id = p2.Mother_id
   AND p1.Person_id != p2.Person_id;

select * from Conections;