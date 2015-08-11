-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2015 at 02:09 PM
-- Server version: 5.6.21
-- PHP Version: 5.5.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `master`
--

-- --------------------------------------------------------

--
-- Table structure for table `favorite`
--

CREATE TABLE IF NOT EXISTS `favorite` (
`id` int(11) NOT NULL,
  `owner_user_id` int(11) DEFAULT NULL,
  `involved_type` int(11) DEFAULT NULL,
  `involved_topic_id` int(11) DEFAULT NULL,
  `involved_reply_id` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE IF NOT EXISTS `inventory` (
`id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `inv1` varchar(4) DEFAULT NULL,
  `inv2` varchar(4) DEFAULT NULL,
  `inv3` varchar(4) DEFAULT NULL,
  `inv4` varchar(4) DEFAULT NULL,
  `inv5` varchar(4) DEFAULT NULL,
  `inv6` varchar(4) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE IF NOT EXISTS `item` (
`id` int(11) NOT NULL,
  `itemid` varchar(3) NOT NULL,
  `name` varchar(40) NOT NULL,
  `zh_cn_name` varchar(20) NOT NULL,
  `cost` varchar(10) NOT NULL,
  `updated` varchar(40) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`id`, `itemid`, `name`, `zh_cn_name`, `cost`, `updated`) VALUES
(1, '28', 'Clarity', '', '50', '2015-08-01 23:30:51'),
(2, '75', 'Iron Branch', '', '50', '2015-08-01 23:30:51'),
(3, '95', 'Observer Ward', '', '75', '2015-08-01 23:30:51'),
(4, '132', 'Smoke of Deceit', '', '100', '2015-08-01 23:30:51'),
(5, '141', 'Town Portal Scroll', '', '100', '2015-08-01 23:30:51'),
(6, '68', 'Healing Salve', '', '110', '2015-08-01 23:30:51'),
(7, '4', 'Animal Courier', '', '120', '2015-08-01 23:30:52'),
(8, '140', 'Tango', '', '125', '2015-08-01 23:30:52'),
(9, '55', 'Gauntlets of Strength', '', '150', '2015-08-01 23:30:52'),
(10, '83', 'Mantle of Intelligence', '', '150', '2015-08-01 23:30:52'),
(11, '130', 'Slippers of Agility', '', '150', '2015-08-01 23:30:52'),
(12, '175', 'Enchanted Mango', '', '150', '2015-08-01 23:30:52'),
(13, '27', 'Circlet', '', '165', '2015-08-01 23:30:52'),
(14, '43', 'Dust of Appearance', '', '180', '2015-08-01 23:30:52'),
(15, '80', 'Magic Stick', '', '200', '2015-08-01 23:30:52'),
(16, '114', 'Ring of Protection', '', '200', '2015-08-01 23:30:52'),
(17, '125', 'Sentry Ward', '', '200', '2015-08-01 23:30:52'),
(18, '138', 'Stout Shield', '', '200', '2015-08-01 23:30:52'),
(19, '51', 'Flying Courier', '', '220', '2015-08-01 23:30:52'),
(20, '107', 'Quelling Blade', '', '225', '2015-08-01 23:30:52'),
(21, '97', 'Orb of Venom', '', '275', '2015-08-01 23:30:52'),
(22, '119', 'Sage&#039;s Mask', '', '325', '2015-08-01 23:30:52'),
(23, '115', 'Ring of Regen', '', '350', '2015-08-01 23:30:52'),
(24, '15', 'Blades of Attack', '', '420', '2015-08-01 23:30:52'),
(25, '9', 'Band of Elvenskin', '', '450', '2015-08-01 23:30:52'),
(26, '11', 'Belt of Strength', '', '450', '2015-08-01 23:30:52'),
(27, '18', 'Boots of Speed', '', '450', '2015-08-01 23:30:52'),
(28, '116', 'Robe of the Magi', '', '450', '2015-08-01 23:30:52'),
(29, '81', 'Magic Wand', '', '465', '2015-08-01 23:30:52'),
(30, '93', 'Null Talisman', '', '470', '2015-08-01 23:30:52'),
(31, '152', 'Wraith Band', '', '485', '2015-08-01 23:30:52'),
(32, '58', 'Gloves of Haste', '', '500', '2015-08-01 23:30:52'),
(33, '21', 'Bracer', '', '525', '2015-08-01 23:30:52'),
(34, '112', 'Ring of Basilius', '', '525', '2015-08-01 23:30:52'),
(35, '25', 'Chainmail', '', '550', '2015-08-01 23:30:52'),
(36, '30', 'Cloak', '', '550', '2015-08-01 23:30:52'),
(37, '104', 'Poor Man&#039;s Shield', '', '550', '2015-08-01 23:30:52'),
(38, '67', 'Headdress', '', '600', '2015-08-01 23:30:52'),
(39, '20', 'Bottle', '', '700', '2015-08-01 23:30:52'),
(40, '23', 'Buckler', '', '800', '2015-08-01 23:30:53'),
(41, '135', 'Soul Ring', '', '800', '2015-08-01 23:30:53'),
(42, '106', 'Quarterstaff', '', '875', '2015-08-01 23:30:53'),
(43, '113', 'Ring of Health', '', '875', '2015-08-01 23:30:53'),
(44, '144', 'Urn of Shadows', '', '875', '2015-08-01 23:30:53'),
(45, '150', 'Void Stone', '', '875', '2015-08-01 23:30:53'),
(46, '45', 'Energy Booster', '', '900', '2015-08-01 23:30:53'),
(47, '56', 'Gem of True Sight', '', '900', '2015-08-01 23:30:53'),
(48, '90', 'Morbid Mask', '', '900', '2015-08-01 23:30:53'),
(49, '71', 'Helm of Iron Will', '', '950', '2015-08-01 23:30:53'),
(50, '14', 'Blade of Alacrity', '', '1000', '2015-08-01 23:30:53'),
(51, '26', 'Cheese', '', '1000', '2015-08-01 23:30:53'),
(52, '96', 'Ogre Club', '', '1000', '2015-08-01 23:30:53'),
(53, '137', 'Staff of Wizardry', '', '1000', '2015-08-01 23:30:53'),
(54, '142', 'Tranquil Boots', '', '1000', '2015-08-01 23:30:53'),
(55, '111', 'Ring of Aquila', '', '1010', '2015-08-01 23:30:53'),
(56, '148', 'Vitality Booster', '', '1100', '2015-08-01 23:30:53'),
(57, '22', 'Broadsword', '', '1200', '2015-08-01 23:30:53'),
(58, '85', 'Medallion of Courage', '', '1200', '2015-08-01 23:30:53'),
(59, '103', 'Point Booster', '', '1200', '2015-08-01 23:30:53'),
(60, '100', 'Phase Boots', '', '1290', '2015-08-01 23:30:53'),
(61, '5', 'Arcane Boots', '', '1350', '2015-08-01 23:30:53'),
(62, '29', 'Claymore', '', '1400', '2015-08-01 23:30:53'),
(63, '102', 'Platemail', '', '1400', '2015-08-01 23:30:53'),
(64, '105', 'Power Treads', '', '1400', '2015-08-01 23:30:54'),
(65, '126', 'Shadow Amulet', '', '1400', '2015-08-01 23:30:54'),
(66, '164', 'Power Treads (Str)', '', '1400', '2015-08-01 23:30:54'),
(67, '163', 'Power Treads (Int)', '', '1400', '2015-08-01 23:30:54'),
(68, '162', 'Power Treads (Agi)', '', '1400', '2015-08-01 23:30:54'),
(69, '57', 'Ghost Scepter', '', '1500', '2015-08-01 23:30:54'),
(70, '76', 'Javelin', '', '1500', '2015-08-01 23:30:54'),
(71, '2', 'Aegis of the Immortal', '', '1600', '2015-08-01 23:30:54'),
(72, '87', 'Mithril Hammer', '', '1600', '2015-08-01 23:30:54'),
(73, '94', 'Oblivion Staff', '', '1650', '2015-08-01 23:30:54'),
(74, '99', 'Perseverance', '', '1750', '2015-08-01 23:30:54'),
(75, '84', 'Mask of Madness', '', '1800', '2015-08-01 23:30:54'),
(76, '139', 'Talisman of Evasion', '', '1800', '2015-08-01 23:30:54'),
(77, '42', 'Drum of Endurance', '', '1850', '2015-08-01 23:30:54'),
(78, '72', 'Helm of the Dominator', '', '1850', '2015-08-01 23:30:54'),
(79, '176', 'Glimmer Cape', '', '1950', '2015-08-01 23:30:54'),
(80, '74', 'Hyperstone', '', '2000', '2015-08-01 23:30:54'),
(81, '66', 'Hand of Midas', '', '2050', '2015-08-01 23:30:54'),
(82, '121', 'Sange', '', '2050', '2015-08-01 23:30:54'),
(83, '154', 'Yasha', '', '2050', '2015-08-01 23:30:54'),
(84, '143', 'Ultimate Orb', '', '2100', '2015-08-01 23:30:54'),
(85, '34', 'Crystalys', '', '2120', '2015-08-01 23:30:54'),
(86, '73', 'Hood of Defiance', '', '2125', '2015-08-01 23:30:54'),
(87, '145', 'Vanguard', '', '2175', '2015-08-01 23:30:54'),
(88, '13', 'Blade Mail', '', '2200', '2015-08-01 23:30:54'),
(89, '16', 'Blink Dagger', '', '2250', '2015-08-01 23:30:54'),
(90, '53', 'Force Staff', '', '2250', '2015-08-01 23:30:54'),
(91, '86', 'Mekansm', '', '2300', '2015-08-01 23:30:54'),
(92, '149', 'Vladmir&#039;s Offering', '', '2325', '2015-08-01 23:30:54'),
(93, '7', 'Armlet of Mordiggian', '', '2370', '2015-08-01 23:30:54'),
(94, '37', 'Demon Edge', '', '2400', '2015-08-01 23:30:54'),
(95, '19', 'Boots of Travel', '', '2450', '2015-08-01 23:30:54'),
(96, '146', 'Veil of Discord', '', '2520', '2015-08-01 23:30:54'),
(97, '91', 'Mystic Staff', '', '2700', '2015-08-01 23:30:55'),
(98, '160', 'Necronomicon 1', '', '2700', '2015-08-01 23:30:55'),
(99, '155', 'Dagon 1', '', '2720', '2015-08-01 23:30:55'),
(100, '79', 'Maelstrom', '', '2800', '2015-08-01 23:30:55'),
(101, '127', 'Shadow Blade', '', '2800', '2015-08-01 23:30:55'),
(102, '47', 'Eul&#039;s Scepter of Divinity', '', '2850', '2015-08-01 23:30:55'),
(103, '129', 'Skull Basher', '', '2950', '2015-08-01 23:30:55'),
(104, '109', 'Reaver', '', '3000', '2015-08-01 23:30:55'),
(105, '183', 'Solar Crest', '', '3000', '2015-08-01 23:30:55'),
(106, '117', 'Rod of Atos', '', '3100', '2015-08-01 23:30:55'),
(107, '40', 'Diffusal Blade', '', '3150', '2015-08-01 23:30:55'),
(108, '44', 'Eaglesong', '', '3200', '2015-08-01 23:30:55'),
(109, '134', 'Soul Booster', '', '3200', '2015-08-01 23:30:55'),
(110, '39', 'Desolator', '', '3500', '2015-08-01 23:30:55'),
(111, '101', 'Pipe of Insight', '', '3525', '2015-08-01 23:30:55'),
(112, '33', 'Crimson Guard', '', '3800', '2015-08-01 23:30:55'),
(113, '118', 'Sacred Relic', '', '3800', '2015-08-01 23:30:55'),
(114, '70', 'Heaven&#039;s Halberd', '', '3850', '2015-08-01 23:30:55'),
(115, '159', 'Diffusal Blade 2', '', '3850', '2015-08-01 23:30:55'),
(116, '161', 'Necronomicon 2', '', '3950', '2015-08-01 23:30:55'),
(117, '156', 'Dagon 2', '', '3970', '2015-08-01 23:30:55'),
(118, '12', 'Black King Bar', '', '3975', '2015-08-01 23:30:55'),
(119, '178', 'Lotus Orb', '', '4050', '2015-08-01 23:30:55'),
(120, '98', 'Orchid Malevolence', '', '4075', '2015-08-01 23:30:55'),
(121, '120', 'Sange and Yasha', '', '4100', '2015-08-01 23:30:55'),
(122, '3', 'Aghanim&#039;s Scepter', '', '4200', '2015-08-01 23:30:55'),
(123, '179', 'Moon Shard', '', '4300', '2015-08-01 23:30:55'),
(124, '182', 'Teleport Level 2', '', '4450', '2015-08-01 23:30:56'),
(125, '10', 'Battle Fury', '', '4575', '2015-08-01 23:30:56'),
(126, '46', 'Ethereal Blade', '', '4700', '2015-08-01 23:30:56'),
(127, '128', 'Shiva&#039;s Guard', '', '4700', '2015-08-01 23:30:56'),
(128, '17', 'Bloodstone', '', '4900', '2015-08-01 23:30:56'),
(129, '82', 'Manta Style', '', '4950', '2015-08-01 23:30:56'),
(130, '78', 'Linken&#039;s Sphere', '', '5175', '2015-08-01 23:30:56'),
(131, '92', 'Necronomicon', '', '5200', '2015-08-01 23:30:56'),
(132, '181', 'Silver Edge', '', '5200', '2015-08-01 23:30:56'),
(133, '157', 'Dagon 3', '', '5220', '2015-08-01 23:30:56'),
(134, '108', 'Radiance', '', '5225', '2015-08-01 23:30:56'),
(135, '8', 'Assault Cuirass', '', '5250', '2015-08-01 23:30:56'),
(136, '110', 'Refresher Orb', '', '5300', '2015-08-01 23:30:56'),
(137, '177', 'Guardian Greaves', '', '5300', '2015-08-01 23:30:56'),
(138, '89', 'Monkey King Bar', '', '5400', '2015-08-01 23:30:56'),
(139, '69', 'Heart of Tarrasque', '', '5500', '2015-08-01 23:30:56'),
(140, '35', 'Daedalus', '', '5520', '2015-08-01 23:30:56'),
(141, '48', 'Eye of Skadi', '', '5675', '2015-08-01 23:30:56'),
(142, '124', 'Scythe of Vyse', '', '5675', '2015-08-01 23:30:56'),
(143, '88', 'Mjollnir', '', '5700', '2015-08-01 23:30:56'),
(144, '24', 'Butterfly', '', '5875', '2015-08-01 23:30:56'),
(145, '180', 'Octarine Core', '', '5900', '2015-08-01 23:30:56'),
(146, '122', 'Satanic', '', '5950', '2015-08-01 23:30:56'),
(147, '41', 'Divine Rapier', '', '6200', '2015-08-01 23:30:56'),
(148, '158', 'Dagon 4', '', '6470', '2015-08-01 23:30:56'),
(149, '1', 'Abyssal Blade', '', '6750', '2015-08-01 23:30:56'),
(150, '36', 'Dagon 5', '', '7720', '2015-08-01 23:30:56');

-- --------------------------------------------------------

--
-- Table structure for table `node`
--

CREATE TABLE IF NOT EXISTS `node` (
`id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `slug` varchar(40) DEFAULT NULL,
  `thumb` varchar(40) DEFAULT NULL,
  `introduction` varchar(80) DEFAULT NULL,
  `created` varchar(20) DEFAULT NULL,
  `updated` varchar(20) DEFAULT NULL,
  `plane_id` int(11) DEFAULT NULL,
  `topic_count` int(11) DEFAULT NULL,
  `custom_style` text,
  `limit_reputation` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `node`
--

INSERT INTO `node` (`id`, `name`, `slug`, `thumb`, `introduction`, `created`, `updated`, `plane_id`, `topic_count`, `custom_style`, `limit_reputation`) VALUES
(1, '新闻', 'news', 'news', '新闻', 'admin', 'admin', 1, NULL, NULL, NULL),
(2, '社区', 'item', 'item', '物品', 'admin', 'admin', 2, NULL, NULL, NULL),
(3, '赛事', 'player', 'player', '玩家', 'admin', 'admin', 7, NULL, NULL, NULL),
(4, '攻略', 'match', 'match', '比赛', 'admin', 'admin', 6, NULL, NULL, NULL),
(5, '集锦', 'strategy', 'strategy', '攻略', 'admin', 'admin', 4, NULL, NULL, NULL),
(6, '资料', 'video', 'video', '视频', 'admin', 'admin', 5, NULL, NULL, NULL),
(7, '更新', 'news', 'news', '新闻', 'admin', 'admin', 3, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE IF NOT EXISTS `notification` (
`id` int(11) NOT NULL,
  `content` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `involved_type` int(11) DEFAULT NULL,
  `involved_user_id` int(11) DEFAULT NULL,
  `involved_topic_id` int(11) DEFAULT NULL,
  `involved_reply_id` int(11) DEFAULT NULL,
  `trigger_user_id` int(11) DEFAULT NULL,
  `occurrence_time` datetime DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `notification`
--


-- --------------------------------------------------------

--
-- Table structure for table `panel`
--

CREATE TABLE IF NOT EXISTS `panel` (
`id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `describe` varchar(40) DEFAULT NULL,
  `created` varchar(20) DEFAULT NULL,
  `updated` varchar(20) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `panel`
--

-- --------------------------------------------------------

--
-- Table structure for table `plane`
--

CREATE TABLE IF NOT EXISTS `plane` (
`id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `describe` varchar(40) DEFAULT NULL,
  `created` varchar(20) DEFAULT NULL,
  `updated` varchar(20) DEFAULT NULL,
  `owner` varchar(20) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `plane`
--

INSERT INTO `plane` (`id`, `name`, `describe`, `created`, `updated`, `owner`) VALUES
(1, 'news', '新闻', 'admin', 'admin', NULL),
(2, 'events', '赛事', 'admin', 'admin', NULL),
(3, 'forum', '社区', 'admin', 'admin', NULL),
(4, 'strategy', '攻略', 'admin', 'admin', NULL),
(5, 'data', '资料', 'admin', 'admin', NULL),
(6, 'update', '更新', 'admin', 'admin', NULL),
(7, 'player', '玩家', 'admin', 'admin', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reply`
--

CREATE TABLE IF NOT EXISTS `reply` (
`id` int(11) NOT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `content` text,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `up_vote` int(11) DEFAULT NULL,
  `down_vote` int(11) DEFAULT NULL,
  `last_touched` datetime DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `reply`
--

-- --------------------------------------------------------

--
-- Table structure for table `topic`
--

CREATE TABLE IF NOT EXISTS `topic` (
`id` int(11) NOT NULL,
  `title` text,
  `content` text,
  `status` int(11) DEFAULT NULL,
  `hits` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `node_id` int(11) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `reply_count` int(11) DEFAULT NULL,
  `last_replied_by` varchar(20) DEFAULT NULL,
  `last_replied_time` datetime DEFAULT NULL,
  `up_vote` int(11) DEFAULT NULL,
  `down_vote` int(11) DEFAULT NULL,
  `last_touched` datetime DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `topic`
--
--
-- Triggers `topic`
--
DELIMITER //
CREATE TRIGGER `topic_delete_trigger` BEFORE DELETE ON `topic`
 FOR EACH ROW BEGIN
        DELETE FROM reply WHERE reply.topic_id = OLD.id;
        DELETE FROM notification WHERE notification.involved_topic_id = OLD.id;
    END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE IF NOT EXISTS `transaction` (
`id` int(11) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `reward` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `current_balance` int(11) DEFAULT NULL,
  `involved_user_id` int(11) DEFAULT NULL,
  `involved_topic_id` int(11) DEFAULT NULL,
  `involved_reply_id` int(11) DEFAULT NULL,
  `occurrence_time` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
`uid` int(11) NOT NULL,
  `email` varchar(40) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `nickname` varchar(20) DEFAULT NULL,
  `avatar` varchar(20) DEFAULT 'nevermore',
  `signature` varchar(120) DEFAULT NULL,
  `location` varchar(40) DEFAULT NULL,
  `website` varchar(120) DEFAULT NULL,
  `inventory` int(11) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `gold` int(11) DEFAULT '625',
  `reputation` int(11) DEFAULT NULL,
  `self_intro` text,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `weibo` varchar(20) DEFAULT NULL,
  `fvteam` varchar(20) DEFAULT NULL,
  `steamid` varchar(20) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--
--
-- Triggers `user`
--
DELIMITER //
CREATE TRIGGER `user_delete_trigger` BEFORE DELETE ON `user`
 FOR EACH ROW BEGIN
        DELETE FROM topic WHERE topic.author_id = OLD.uid;
        DELETE FROM reply WHERE reply.author_id = OLD.uid;
        DELETE FROM notification WHERE notification.trigger_user_id = OLD.uid;
        DELETE FROM notification WHERE notification.involved_user_id = OLD.uid;
    END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `vote`
--

CREATE TABLE IF NOT EXISTS `vote` (
  `id` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL,
  `involved_type` int(11) DEFAULT NULL,
  `involved_user_id` int(11) DEFAULT NULL,
  `involved_topic_id` int(11) DEFAULT NULL,
  `involved_reply_id` int(11) DEFAULT NULL,
  `trigger_user_id` int(11) DEFAULT NULL,
  `occurrence_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `favorite`
--
ALTER TABLE `favorite`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `node`
--
ALTER TABLE `node`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `panel`
--
ALTER TABLE `panel`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `plane`
--
ALTER TABLE `plane`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reply`
--
ALTER TABLE `reply`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `topic`
--
ALTER TABLE `topic`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
 ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `vote`
--
ALTER TABLE `vote`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `favorite`
--
ALTER TABLE `favorite`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `node`
--
ALTER TABLE `node`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `panel`
--
ALTER TABLE `panel`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `plane`
--
ALTER TABLE `plane`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `reply`
--
ALTER TABLE `reply`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `topic`
--
ALTER TABLE `topic`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
