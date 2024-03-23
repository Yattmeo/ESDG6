-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'DoctorAvailability'
-- 
-- ---
CREATE DATABASE IF NOT EXISTS `schedulingDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `schedulingDB`;

DROP TABLE IF EXISTS `DoctorAvailability`;

DROP TABLE IF EXISTS `Doctors`;

CREATE TABLE `Doctors` (
  `DoctorID` INTEGER NOT NULL AUTO_INCREMENT,
  `Specialty` VARCHAR(255),
  `Name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`DoctorID`)
);

CREATE TABLE `DoctorAvailability` (
  `AppointmentID` INTEGER NOT NULL AUTO_INCREMENT,
  `Date` DATE NOT NULL,
  `SlotNum` TINYINT NOT NULL,
  `DoctorID_Doctors` INT NOT NULL,
  PRIMARY KEY (`AppointmentID`),
  FOREIGN KEY (`DoctorID_Doctors`) REFERENCES `Doctors` (`DoctorID`)
);


-- ---
-- Table Properties
-- ---

-- ALTER TABLE `DoctorAvailability` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Doctors` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `DoctorAvailability` (`AppointmentID`,`Date`,`SlotNum`,`DoctorID_Doctors`) VALUES
-- ('','','','');
-- INSERT INTO `Doctors` (`DoctorID`,`Specialty`,`Name`) VALUES
-- ('','','');