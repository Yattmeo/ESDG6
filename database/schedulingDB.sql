-- Globals
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET FOREIGN_KEY_CHECKS=0;

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS `schedulingDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `schedulingDB`;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS `DoctorAvailability`;
DROP TABLE IF EXISTS `Doctors`;

-- Create Doctors table
CREATE TABLE `Doctors` (
  `DoctorID` INTEGER NOT NULL AUTO_INCREMENT,
  `Specialty` VARCHAR(255),
  `Name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`DoctorID`)
);

-- Create DoctorAvailability table
CREATE TABLE `DoctorAvailability` (
  `AppointmentID` INTEGER NOT NULL AUTO_INCREMENT,
  `Date` DATE NOT NULL,
  `SlotNum` TINYINT NOT NULL,
  `DoctorID_Doctors` INT NOT NULL,
  PRIMARY KEY (`AppointmentID`),
  FOREIGN KEY (`DoctorID_Doctors`) REFERENCES `Doctors` (`DoctorID`)
);

-- Insert dummy data into Doctors table
INSERT INTO `Doctors` (`Specialty`, `Name`) VALUES
('Cardiologist', 'Dr. Smith'),
('Neurologist', 'Dr. Johnson'),
('Pediatrician', 'Dr. Williams'),
('Dermatologist', 'Dr. Brown');

-- Insert dummy data into DoctorAvailability table
INSERT INTO `DoctorAvailability` (`Date`, `SlotNum`, `DoctorID_Doctors`) VALUES
('2024-03-25', 1, 1),
('2024-03-25', 2, 2),
('2024-03-26', 1, 3),
('2024-03-26', 2, 4);
