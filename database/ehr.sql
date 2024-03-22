-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `EHR`
--
CREATE DATABASE IF NOT EXISTS `EHR` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `EHR`;

-- --------------------------------------------------------

--
-- Table structure for table `ehr`
--

DROP TABLE IF EXISTS `ehr`;
CREATE TABLE IF NOT EXISTS `ehr` (
  `patient_id` int NOT NULL,
  `medical_conditions` (varchar(255)),
  `allergies` varchar(255),
  `medications` varchar(255),
  `surgeries` varchar(255),
  `immunisations` varchar(255),
  `family_medical_history` varchar(255),
  `past_appointments` datetime,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ehr`
--

INSERT INTO `ehr` (`patient_id`, `medical_conditions`, `allergies`, `medications`, `surgeries`, `immunisations`, `family_medical_history`, `past_appointments`) VALUES
(1, 'Hypertension', 'Penicillin', 'Lisinopril', 'Appendectomy', 'Flu Vaccine', 'Heart disease in family', '["2023-01-15T10:30:00Z", "2022-11-10T08:45:00Z"]'),
    (2, 'Diabetes', NULL, 'Metformin', NULL, NULL, NULL, '["2022-12-20T09:15:00Z", "2023-02-28T14:00:00Z"]'),
    (3, 'Asthma', '["Aspirin", "Dust"]', 'Albuterol', 'Tonsillectomy', 'Tdap Vaccine', 'Asthma in family', '["2023-03-05T11:00:00Z", "2022-10-02T12:30:00Z"]');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
