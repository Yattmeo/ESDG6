CREATE DATABASE IF NOT EXISTS `USERDETAILS` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `USERDETAILS`;

DROP TABLE IF EXISTS `USERDETAILS`;
CREATE TABLE IF NOT EXISTS `USERDETAILS` (
  User_ID INT PRIMARY KEY,
  phone_number BIGINT,
  email VARCHAR(255),
  address VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `USERDETAILS` (`User_ID`, `phone_number`, `email`, `address`) VALUES
    (1, 1234567890, 'john@example.com', '123 Main Street'),
    (2, 9876543210, 'jane@example.com', '456 Elm Street'),
    (3, 5551234567, 'alice@example.com', '789 Oak Avenue');
COMMIT;