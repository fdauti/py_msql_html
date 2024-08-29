-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 08, 2021 at 11:33 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `proj_2`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `name` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `phone` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`name`, `username`, `password`, `phone`, `email`, `address`) VALUES
('admin admin', 'admin', 'admin123', '111-111-7777', 'fdauti@myseneca.ca', 'Seneca College'),
('Fatjon Dauti', 'fotjon', 'fotjon123', '123456789', 'fdauti@myseneca.ca', 'North York'),
('second user', 'user2', 'user2123', '222-111-7777', 'user@email.com', 'Toronto'),
('test user', 'user3', 'user3123', '333-111-7777', 'user3@email.com', 'Toronto');

-- --------------------------------------------------------

--
-- Table structure for table `claims`
--

CREATE TABLE `claims` (
  `claim_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `serial_no` varchar(20) NOT NULL,
  `date` varchar(30) NOT NULL,
  `issue` varchar(200) NOT NULL,
  `approval` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `claims`
--

INSERT INTO `claims` (`claim_id`, `username`, `serial_no`, `date`, `issue`, `approval`) VALUES
(3, 'fotjon', 'dell222', '2021-08-07', 'ljlk', 'rejected'),
(4, 'fotjon', 'p222', '2021-01-05', 'january claim', ''),
(5, 'fotjon', 'p222', '2021-07-07', 'july claim', 'approved'),
(7, 'user3', 'dell222', '2021-02-07', 'february claim user 2', '');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `username` varchar(30) NOT NULL,
  `prod_name` varchar(40) NOT NULL,
  `serial_no` varchar(20) NOT NULL,
  `purch_date` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`username`, `prod_name`, `serial_no`, `purch_date`) VALUES
('user3', 'Dell laptop', 'dell222', '2021-08-01'),
('fotjon', 'prod1', 'p111', '2021-08-05'),
('fotjon', 'prod2', 'p222', '2021-08-06'),
('fotjon', 'prod3', 'p333', '2021-08-14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `claims`
--
ALTER TABLE `claims`
  ADD PRIMARY KEY (`claim_id`),
  ADD KEY `FK_username` (`username`),
  ADD KEY `FK_serialno` (`serial_no`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`serial_no`),
  ADD KEY `FK_username_p` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `claims`
--
ALTER TABLE `claims`
  MODIFY `claim_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `claims`
--
ALTER TABLE `claims`
  ADD CONSTRAINT `FK_serialno` FOREIGN KEY (`serial_no`) REFERENCES `products` (`serial_no`),
  ADD CONSTRAINT `FK_username` FOREIGN KEY (`username`) REFERENCES `accounts` (`username`),
  ADD CONSTRAINT `serial_number` FOREIGN KEY (`serial_no`) REFERENCES `products` (`serial_no`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `FK_username_p` FOREIGN KEY (`username`) REFERENCES `accounts` (`username`),
  ADD CONSTRAINT `username` FOREIGN KEY (`username`) REFERENCES `accounts` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
