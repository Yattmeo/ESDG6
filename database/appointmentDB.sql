-- Globals
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET FOREIGN_KEY_CHECKS=0;

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS `APPOINTMENTDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `APPOINTMENTDB`;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS `Appointments`;
DROP TABLE IF EXISTS `Doctors`;
DROP TABLE IF EXISTS `Patients`;

-- Create Doctors table
CREATE TABLE `Doctors` (
  `DoctorID` INTEGER NOT NULL,
  `Specialty` VARCHAR(255) NULL DEFAULT NULL,
  `Name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`DoctorID`)
);

-- Create Patients table
CREATE TABLE `Patients` (
  `PatientID` INTEGER NOT NULL,
  `Name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`PatientID`)
);

-- Create Appointments table
CREATE TABLE `Appointments` (
  `AppointmentID` INTEGER NOT NULL AUTO_INCREMENT,
  `Datetime` DATETIME NOT NULL,
  `Slot` INTEGER NOT NULL,
  `DoctorID_Doctors` INTEGER NOT NULL,
  `PatientID_Patients` INTEGER NOT NULL,
  `Status` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`AppointmentID`),
  FOREIGN KEY (`DoctorID_Doctors`) REFERENCES `Doctors` (`DoctorID`),
  FOREIGN KEY (`PatientID_Patients`) REFERENCES `Patients` (`PatientID`)
);

-- Insert dummy data into Doctors table
INSERT INTO `Doctors` (`DoctorID`,`Specialty`, `Name`) VALUES
('1','Cardiologist', 'Dr. Smith'),
('2','Neurologist', 'Dr. Johnson'),
('3','Pediatrician', 'Dr. Williams'),
('4','Dermatologist', 'Dr. Brown');

-- Insert dummy data into Patients table
INSERT INTO `Patients` (`PatientID`,`Name`) VALUES
('1','John Doe'),
('2','Jane Smith'),
('3','Michael Johnson'),
('4','Emily Williams'),
('5','David Brown');

-- Insert dummy data into Appointments table
INSERT INTO `Appointments` (`Datetime`, `Slot`, `DoctorID_Doctors`, `PatientID_Patients`, `Status`) VALUES
('2024-03-25 08:00:00', 1, 1, 1, 'Confirmed'),
('2024-03-25 10:00:00', 2, 2, 2, 'Confirmed'),
('2024-03-26 09:00:00', 1, 3, 3, 'Cancelled'),
('2024-03-26 11:00:00', 2, 4, 4, 'Confirmed'),
('2024-03-27 08:30:00', 1, 1, 5, 'Confirmed');

-- Set foreign key checks back to 1
SET FOREIGN_KEY_CHECKS=1;
