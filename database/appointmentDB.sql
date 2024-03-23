-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'Doctors'
-- 
-- ---
CREATE DATABASE IF NOT EXISTS `appointmentDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `appointmentDB`;

DROP TABLE IF EXISTS `Doctors`;
		
CREATE TABLE `Doctors` (
  `DoctorID` INTEGER NOT NULL AUTO_INCREMENT,
  `Specialty` VARCHAR(255) NULL DEFAULT NULL,
  `Name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`DoctorID`)
);

-- ---
-- Table 'Patients'
-- 
-- ---

DROP TABLE IF EXISTS `Patients`;
		
CREATE TABLE `Patients` (
  `PatientID` INTEGER NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`PatientID`)
);

-- ---
-- Table 'Appointments'
-- 
-- ---

DROP TABLE IF EXISTS `Appointments`;
		
CREATE TABLE `Appointments` (
  `AppointmentID` INTEGER NOT NULL AUTO_INCREMENT,
  `Datetime` DATETIME NOT NULL,
  `Slot` INTEGER NOT NULL,
  `DoctorID_Doctors` INTEGER NOT NULL,
  `PatientID_Patients` INTEGER NOT NULL,
  `Status` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`AppointmentID`)
);

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `Appointments` ADD FOREIGN KEY (DoctorID_Doctors) REFERENCES `Doctors` (`DoctorID`);
ALTER TABLE `Appointments` ADD FOREIGN KEY (PatientID_Patients) REFERENCES `Patients` (`PatientID`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `Doctors` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Patients` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Appointments` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `Doctors` (`DoctorID`,`Specialty`,`Name`) VALUES
-- ('','','');
-- INSERT INTO `Patients` (`PatientID`,`Name`) VALUES
-- ('','');
-- INSERT INTO `Appointments` (`AppointmentID`,`Datetime`,`Clinic`,`DoctorID_Doctors`,`PatientID_Patients`) VALUES
-- ('','','','','');