use bloodbank;

-- Adding 10 random records to the Donor table:
INSERT INTO Donor (Donor_ID, Blood_Group, Name, Medical_History, Age, Address)
VALUES
('D001', 'A+', 'John Smith', 'None', 27, '123 Main St.'),
('D002', 'B+', 'Emily Johnson', 'High blood pressure', 35, '456 Elm St.'),
('D003', 'O+', 'Adam Lee', 'Allergies', 42, '789 Maple St.'),
('D004', 'AB+', 'Lila Patel', 'None', 21, '321 Oak St.'),
('D005', 'A-', 'Tyler Davis', 'Diabetes', 29, '654 Pine St.'),
('D006', 'B-', 'Sophia Wilson', 'None', 30, '987 Cedar St.'),
('D007', 'O-', 'Michael Brown', 'Asthma', 46, '246 Birch St.'),
('D008', 'AB-', 'Avery Taylor', 'None', 25, '369 Spruce St.'),
('D009', 'A+', 'Noah Thomas', 'None', 32, '753 Hickory St.'),
('D010', 'O+', 'Olivia Hernandez', 'None', 39, '159 Willow St.');

-- Adding 10 random records to the Patient table:
INSERT INTO Patient (Name, Patient_ID, Address, Age, Blood_Group, Date_required)
VALUES
('Sarah Johnson', 'P001', '321 Oak St.', 25, 'A+', '2023-05-10'),
('Thomas Anderson', 'P002', '789 Maple St.', 37, 'B+', '2023-04-25'),
('Ava Garcia', 'P003', '456 Elm St.', 43, 'O+', '2023-05-05'),
('William Rodriguez', 'P004', '987 Cedar St.', 29, 'AB+', '2023-04-30'),
('Mia Martinez', 'P005', '246 Birch St.', 36, 'A-', '2023-05-12'),
('Ethan Gonzalez', 'P006', '753 Hickory St.', 51, 'B-', '2023-05-01'),
('Sophia Lewis', 'P007', '123 Main St.', 27, 'O-', '2023-05-08'),
('Liam King', 'P008', '369 Spruce St.', 18, 'AB-', '2023-04-28'),
('Isabella Wright', 'P009', '654 Pine St.', 31, 'A+', '2023-05-14'),
('Michael Scott', 'P010', '159 Willow St.', 45, 'O+', '2023-05-02');

-- Adding 10 random records to the Blood_Component table:
INSERT INTO Blood_Component (Component, Blood_Group, Blood_ID)
VALUES
('Red Blood Cells', 'A+', 'B001'),
('Plasma', 'A+', 'B002'),
('Cryoprecipitate', 'A+', 'B003'),
('Red Blood Cells', 'A-', 'B004'),
('Plasma', 'A-', 'B005'),
('Cryoprecipitate', 'A-', 'B006'),
('Red Blood Cells', 'B+', 'B007'),
('Plasma', 'B+', 'B008'),
('Cryoprecipitate', 'B+', 'B009'),
('Red Blood Cells', 'B-', 'B010'),
('Plasma', 'B-', 'B011'),
('Cryoprecipitate', 'B-', 'B012'),
('Cryoprecipitate', 'AB+', 'B013'),
('Red Blood Cells', 'AB+', 'B014'),
('Plasma', 'AB+', 'B015'),
('Red Blood Cells', 'AB-', 'B016'),
('Plasma', 'AB-', 'B017'),
('Cryoprecipitate', 'AB-', 'B018'),
('Red Blood Cells', 'O+', 'B019'),
('Plasma', 'O+', 'B020'),
('Cryoprecipitate', 'O+', 'B021'),
('Red Blood Cells', 'O-', 'B022'),
('Plasma', 'O-', 'B023'),
('Cryoprecipitate', 'O-', 'B024');

INSERT INTO Inventory (Date_Stored, Expiry_Date, ID, Price, Quantity, Storage_Location, Status, Donor_ID, Blood_ID)
VALUES 
('2023-02-15', '2023-04-15', 'I001', 100, 10, 'Shelf A', 'Available', 'D001', 'B001'),
('2023-02-01', '2023-04-01', 'I002', 150, 5, 'Shelf B', 'Expired', 'D002', 'B001'),
('2023-03-01', '2023-05-01', 'I004', 120, 8, 'Shelf D', 'Available', 'D004', 'B002'),
('2023-02-25', '2023-04-25', 'I005', 90, 12, 'Shelf E', 'Available', 'D005', 'B003'),
('2023-03-05', '2023-05-05', 'I006', 80, 6, 'Shelf F', 'Available', 'D006', 'B003'),
('2023-02-10', '2023-04-10', 'I007', 70, 3, 'Shelf G', 'Expired', 'D007', 'B004'),
('2023-02-20', '2023-04-20', 'I008', 200, 20, 'Shelf H', 'Available', 'D008', 'B004'),
('2023-01-05', '2023-03-05', 'I009', 150, 7, 'Shelf I', 'Expired', 'D009', 'B005'),
('2023-03-15', '2023-05-15', 'I010', 100, 18, 'Shelf J', 'Available', 'D010', 'B005');


