
CREATE DATABASE USERDETAILS;


USE USERDETAILS;


CREATE TABLE user_details (
    User_ID INT PRIMARY KEY,
    phone_number BIGINT,
    email VARCHAR(255),
    address VARCHAR(255)
);


INSERT INTO user_details (User_ID, phone_number, email, address)
VALUES
    (1, 1234567890, 'john@example.com', '123 Main Street'),
    (2, 9876543210, 'jane@example.com', '456 Elm Street'),
    (3, 5551234567, 'alice@example.com', '789 Oak Avenue');
