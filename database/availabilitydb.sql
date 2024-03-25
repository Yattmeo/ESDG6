
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET FOREIGN_KEY_CHECKS=0;



-- Drop existing tables if they exist
DROP TABLE IF EXISTS `Availability`;
DROP TABLE IF EXISTS `Doctors`;
-- Table for storing availability updates

CREATE TABLE `Doctors` (
  `DoctorID` INTEGER NOT NULL AUTO_INCREMENT,
  `Specialty` VARCHAR(255) NULL DEFAULT NULL,
  `Name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`DoctorID`)
);

CREATE TABLE Availability (
    `doctorID` INT,
    `date` DATE,
    `slots` TEXT,
    PRIMARY KEY(`doctorID`, date)
    FOREIGN KEY (`doctorID`) REFERENCES `Doctors` (`DoctorID`)
);

-- Insert dummy data into Doctors table
INSERT INTO `Doctors` (`Specialty`, `Name`) VALUES
('Cardiologist', 'Dr. Smith'),
('Neurologist', 'Dr. Johnson'),
('Pediatrician', 'Dr. Williams'),
('Dermatologist', 'Dr. Brown');

INSERT INTO Availability (`doctorID`, `date`, `slots`) 
VALUES (1, '2024-05-18', '[930, 1000, 1100, 1200]');

INSERT INTO Availability (`doctorID`, `date`, `slots`) 
VALUES (1, '2024-05-19', '[930, 1000, 1100, 1200]');

INSERT INTO Availability (`doctorID`, `date`, `slots`) 
VALUES (1, '2024-05-20', '[930, 1000, 1100, 1200]');

INSERT INTO Availability (`doctorID`, `date`, `slots`) 
VALUES (2, '2024-05-17', '[930, 1000, 1100, 1200]');

INSERT INTO Availability (`doctorID`, `date`, `slots`) 
VALUES (2, '2024-05-18', '[930, 1000, 1100, 1200]');