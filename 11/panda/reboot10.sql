-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: reboot10
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cabinet`
--

DROP TABLE IF EXISTS `cabinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL COMMENT '机柜名称',
  `idc_id` int(11) DEFAULT NULL COMMENT '所在机房ID',
  `u_num` varchar(10) DEFAULT NULL COMMENT 'U位',
  `power` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COMMENT='机柜表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (5,'005',1,'32U','32A'),(6,'002',7,'1U','20A'),(7,'010',8,'24U','20A');
/*!40000 ALTER TABLE `cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idc`
--

DROP TABLE IF EXISTS `idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL COMMENT '机房英文简写',
  `name_cn` varchar(50) DEFAULT NULL COMMENT '机房中文名',
  `address` varchar(128) DEFAULT NULL COMMENT '机房地址',
  `adminer` varchar(32) DEFAULT NULL COMMENT '机房联系人',
  `phone` varchar(11) DEFAULT NULL COMMENT '联系电话',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='机房表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (1,'syq','sanyuanqiao','san','pc','1821019911'),(7,'hp','hp','hp','wd','111'),(8,'zhaowei','zhaowei','zhaowei','wd','111');
/*!40000 ALTER TABLE `idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idclist`
--

DROP TABLE IF EXISTS `idclist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idclist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '机房名',
  `cabinets` varchar(50) NOT NULL COMMENT '机柜数量',
  `hosts` varchar(50) NOT NULL COMMENT '主机数量',
  `contacts` varchar(50) DEFAULT NULL COMMENT '联系人',
  `telephone` varchar(11) NOT NULL COMMENT '电话',
  `remarks` varchar(10) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='idc列表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idclist`
--

LOCK TABLES `idclist` WRITE;
/*!40000 ALTER TABLE `idclist` DISABLE KEYS */;
INSERT INTO `idclist` VALUES (2,'sdsds','11','11','11','11','11');
/*!40000 ALTER TABLE `idclist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(24) NOT NULL COMMENT '主机名',
  `lan_ip` varchar(24) DEFAULT NULL COMMENT '内网IP',
  `wan_ip` varchar(24) DEFAULT NULL COMMENT '外网IP',
  `cabinet_id` int(11) DEFAULT NULL COMMENT '机柜ID',
  `op` varchar(24) DEFAULT NULL COMMENT '运维负责人',
  `phone` varchar(11) DEFAULT NULL COMMENT '联系电话',
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='服务器表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,'web1','192.168.1.2','202.202.202.100',1,'pc','1831019911'),(2,'web2','192.168.1.3','202.202.202.101',1,'pc','1831019911'),(3,'web3','192.168.1.4','202.202.202.102',1,'pc','1831019911'),(4,'db1','192.168.1.5','202.202.202.103',2,'wd','1821019911'),(5,'db2','192.168.1.6','202.202.202.104',2,'wd','1821019911');
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT 'ç”¨æˆ·å',
  `name_cn` varchar(50) NOT NULL COMMENT 'ä¸­æ–‡å',
  `password` varchar(50) NOT NULL COMMENT 'ç”¨æˆ·å¯†ç ',
  `email` varchar(50) DEFAULT NULL COMMENT 'ç”µå­é‚®ä»¶',
  `mobile` varchar(11) NOT NULL COMMENT 'æ‰‹æœºå·ç ',
  `role` varchar(10) NOT NULL COMMENT '1:sa;2:php;3:ios;4:test',
  `status` tinyint(4) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL COMMENT 'åˆ›å»ºæ—¶é—´',
  `last_time` datetime DEFAULT NULL COMMENT 'æœ€åŽç™»å½•æ—¶é—´',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=latin1 COMMENT='ç”¨æˆ·è¡¨';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (21,'1q11','22222','11','11','11','admin',0,'2016-08-13 12:43:25',NULL),(22,'sss','aaaa','11','111@qq','1111','user',0,'2016-08-13 14:16:36',NULL),(42,'liu','liuziping','11','22','22','user',0,'2016-08-27 09:17:03','2016-09-03 10:39:03'),(44,'reboot','reboot','11','1111@!1.com','11111','CU',0,NULL,NULL),(45,'cc','1111111','11','111@qq','2222222','admin',1,'2016-09-03 10:35:01','2016-09-03 10:35:01'),(51,'aa','bb','cc','dd','dd','ss',0,NULL,NULL),(52,'add','bb','cc','dd','dd','ss',0,NULL,NULL),(57,'ccc','ccc','ce5b428f93ab83af44e2780e51c339e9','111@qq','121212','user',0,NULL,NULL),(59,'pc','pc','0d56a13fff7a4616dc274f34dce72e16','1111@reboot.com','11232131232','admin',0,NULL,NULL),(66,'pc11','pc','0d56a13fff7a4616dc274f34dce72e16','','','CU',0,NULL,NULL),(67,'aaaa','aa','0d56a13fff7a4616dc274f34dce72e16','','','CU',0,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-23 15:15:46
