use bloodbank;

-- Query to retrieve the list of all blood units with their current availability status.
SELECT ID, Component, Blood_Group, Status, Price, Quantity
FROM Inventory
JOIN Blood_Component ON Inventory.Blood_ID = Blood_Component.Blood_ID;

/*Query to retrieve the list of all blood donors along with their personal details and donation history.
The LEFT JOIN is used to include all donors from the "Donor" table, even if they have not
made any donations yet.*/
SELECT D.Donor_ID, D.Name, D.Blood_Group, D.Medical_History, D.Age, D.Address, DH.Date_Stored
FROM Donor D
LEFT JOIN Inventory DH ON D.Donor_ID = DH.Donor_ID
ORDER BY D.Donor_ID;

-- Query to add a new blood donor to the database.
INSERT INTO Donor (Donor_ID, Blood_Group, Name, Medical_History, Age, Address)
VALUES ('D001', 'A+', 'John Doe', 'No medical history', 30, '1234 Elm Street, Springfield, IL');

-- Query to update the information of a blood donor.
UPDATE Donor
SET Blood_Group = 'B+', Name = 'Jane Smith', Medical_History = 'No significant medical history', Age = 35, Address = '5678 Oak Street, Chicago, IL'
WHERE Donor_ID = 'D001';

-- Query to add a new blood unit to the inventory.
INSERT INTO Inventory (Date_Stored, Expiry_Date, ID, Price, Quantity, Storage_Location, Status, Donor_ID, Blood_ID)
VALUES ('2023-04-11', '2023-06-11', 'I001', 50, 1, 'Refrigerator 1, Shelf 3', 'Available', 'D001', 'B001');

-- Query to retrieve the information of all the donors whose blood group is AB+ .
SELECT *
FROM Donor
WHERE Blood_Group = 'AB+';

-- Query to delete the information of a specific donor.
DELETE FROM Donor
WHERE Donor_ID = 'your_donor_id_here';

-- Query to retrieve the list of blood units that are about to expire in the next 30 days.
SELECT *
FROM Inventory
WHERE Expiry_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY);

-- Query to get the Blood ID of a particular combination of Blood Group and Component
SELECT Blood_ID 
FROM Blood_Component 
WHERE blood_group = "A+" AND component = "Red Blood Cells";

-- Query to get the Available blood units in ascending order of Expiry Date
SELECT ID, Component, Expiry_date FROM Inventory_View WHERE Blood_Group = "A+" AND Status = 'Available' ORDER BY Expiry_date;

-- Query to get the Transfusion History of a particular Patient
SELECT t.Patient_ID, i.ID, t.Date_Transfused, i.Donor_ID 
FROM transfusion t 
JOIN inventory i ON t.Unit_ID = i.ID 
WHERE t.Patient_ID = "P001";


