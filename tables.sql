DROP DATABASE IF EXISTS bloodbank;
CREATE DATABASE bloodbank;
USE bloodbank;

DROP TABLE IF EXISTS Donor_Contact_No;
DROP TABLE IF EXISTS Patient_Contact_No;
DROP TABLE IF EXISTS Transfusion;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Donor; 
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS Blood_Component;

CREATE TABLE Donor
(
  Donor_ID VARCHAR(5) NOT NULL,
  Blood_Group VARCHAR(3) NOT NULL,
  Name VARCHAR(255),
  Medical_History VARCHAR(255),
  Age INT,
  Address VARCHAR(255),
  PRIMARY KEY (Donor_ID)
);

CREATE TABLE Patient
(
  Name VARCHAR(255),
  Patient_ID VARCHAR(5) NOT NULL,
  Address VARCHAR(255),
  Age INT,
  Blood_Group VARCHAR(3),
  PRIMARY KEY (Patient_ID)
);

CREATE TABLE Blood_Component
(
  Component VARCHAR(25) NOT NULL,
  Blood_Group VARCHAR(3) NOT NULL,
  Blood_ID VARCHAR(5) NOT NULL,
  PRIMARY KEY (Blood_ID),
  CONSTRAINT uc Unique(COmponent, Blood_Group)
);

CREATE TABLE Donor_Contact_No
(
  Contact_No VARCHAR(11) NOT NULL,
  Donor_ID VARCHAR(5) NOT NULL,
  PRIMARY KEY (Contact_No, Donor_ID),
  FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID)
);

CREATE TABLE Patient_Contact_No
(
  Contact_No VARCHAR(11) NOT NULL,
  Patient_ID VARCHAR(5) NOT NULL,
  PRIMARY KEY (Contact_No, Patient_ID),
  FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Inventory
(
  Date_Stored DATE NOT NULL,
  Expiry_date DATE NOT NULL,
  ID VARCHAR(5) NOT NULL,
  Price INT,
  Quantity INT,
  Storage_Location VARCHAR(255),
  Status VARCHAR(25),
  Donor_ID VARCHAR(5) NOT NULL,
  Blood_ID VARCHAR(5) NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID),
  FOREIGN KEY (Blood_ID) REFERENCES Blood_Component(Blood_ID)
  );
  
CREATE TABLE Transfusion
(
	Unit_Id VARCHAR(5) NOT NULL,
    Patient_Id VARCHAR(5) NOT NULL,
    Date_Transfused DATE NOT NULL,
    PRIMARY KEY(Unit_Id),
    FOREIGN KEY (Unit_Id) REFERENCES Inventory(ID),
    FOREIGN KEY (Patient_Id) REFERENCES Patient(Patient_ID)
    );


CREATE VIEW Blood_Donation_History AS
SELECT 'Donor_ID', 'Date_Stored'
FROM Inventory;

CREATE VIEW Inventory_View AS
SELECT I.ID as ID, I.Date_stored as Date_stored, I.Expiry_Date as Expiry_Date, I.Price as Price, I.Quantity as Quantity,
I.Storage_Location as Storage_Location, I.Status as Status, I.Donor_ID as Donor_ID, B.Blood_Group as Blood_Group, B.Component as Component
FROM
Inventory as I
NATURAL JOIN
Blood_Component as B;
    
SHOW TABLES;