-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2022 at 10:55 AM
-- Server version: 10.1.9-MariaDB
-- PHP Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `librarymanagement`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `BookID` int(8) DEFAULT NULL,
  `BookName` varchar(40) DEFAULT NULL,
  `Author` varchar(30) DEFAULT NULL,
  `Yearoflaunch` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`BookID`, `BookName`, `Author`, `Yearoflaunch`) VALUES
(1254, 'Percy Jackson', 'Rick Riordan', 2010),
(1277, 'Harry Potter', 'JK Rowling', 1997),
(1232, 'Naruto', 'Masashi Kishimoto', 1999),
(1212, 'abc', 'xyz', 2000);

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `M_ID` int(8) DEFAULT NULL,
  `M_Name` varchar(30) DEFAULT NULL,
  `YearOfJoining` int(10) DEFAULT NULL,
  `M_City` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`M_ID`, `M_Name`, `YearOfJoining`, `M_City`) VALUES
(2403, 'Rahul', 2014, 'Jaipur'),
(2152, 'Maldev', 2013, 'Jojawar');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
