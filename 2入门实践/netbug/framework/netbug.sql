-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2016-08-02 17:22:16
-- 服务器版本： 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `netbug`
--
CREATE DATABASE IF NOT EXISTS `netbug` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `netbug`;

-- --------------------------------------------------------

--
-- 表的结构 `layer1`
--

CREATE TABLE IF NOT EXISTS `layer1` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `company` tinytext NOT NULL,
  `url` varchar(500) NOT NULL,
  `add_time` int(11) unsigned NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '-1' COMMENT '-2失败-1未处理1处理成功2处理中',
  PRIMARY KEY (`id`),
  KEY `url` (`url`(255))
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
