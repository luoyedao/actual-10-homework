-- MySQL dump 10.14  Distrib 5.5.47-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: reboot10
-- ------------------------------------------------------
-- Server version	5.5.47-MariaDB

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
  `name` varchar(20) NOT NULL,
  `idc_id` int(11) DEFAULT NULL,
  `u_num` varchar(20) DEFAULT NULL,
  `power` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `idc_id` (`idc_id`),
  CONSTRAINT `cabinet_ibfk_1` FOREIGN KEY (`idc_id`) REFERENCES `idc` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (3,'cabinet02',2,'12U','12'),(4,'cabinet03',4,'1','12'),(5,'cabinet04',4,'12','12');
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
  `name` varchar(20) NOT NULL,
  `name_cn` varchar(50) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `adminer` varchar(20) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (2,'test','test','123','test','12312312312',1),(4,'test2','test2','123','test2','13626223692',123);
/*!40000 ALTER TABLE `idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(20) NOT NULL,
  `lan_ip` varchar(20) DEFAULT NULL,
  `wan_ip` varchar(20) DEFAULT NULL,
  `cabinet_id` int(11) DEFAULT NULL,
  `op` varchar(20) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  KEY `cabinet_id` (`cabinet_id`),
  CONSTRAINT `server_ibfk_1` FOREIGN KEY (`cabinet_id`) REFERENCES `cabinet` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (2,'server01','192.168.3.2','49.77.206.146',3,'yaol','15052235555'),(4,'server02','192.168.3.222','55.57.123.59',4,'yao','15052234444'),(6,'service03','192.168.3.100','55.123.56.127',5,'yaoliang','15055555555');
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
  `name` varchar(20) NOT NULL COMMENT '用户名',
  `name_cn` varchar(50) NOT NULL COMMENT '中文名',
  `password` varchar(50) NOT NULL COMMENT '用户密码',
  `email` varchar(50) DEFAULT NULL COMMENT '电子邮件',
  `mobile` varchar(11) NOT NULL COMMENT '手机号码',
  `role` varchar(10) NOT NULL COMMENT '1:sa;2:php;3:ios;4:test',
  `status` tinyint(4) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `last_time` datetime DEFAULT NULL COMMENT '最后登录时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=latin1 COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (38,'test','test','cd31c5edd043bbd150530e42a0a1abee','yaoliang83@yeah.net','15055555555','admin',0,NULL,NULL),(72,'test1','test1','cd31c5edd043bbd150530e42a0a1abee','test@qq.com','15052237898','user',0,NULL,NULL),(81,'12345','1234','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(82,'123456','123','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(83,'1234567','123','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(84,'12345678','123','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(85,'123456789','123','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(86,'1234567890','123','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(87,'12345678901','123','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(88,'123456789012','123','cd31c5edd043bbd150530e42a0a1abee','','','user',0,NULL,NULL),(91,'admin','admin','cd31c5edd043bbd150530e42a0a1abee','','','admin',0,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work`
--

DROP TABLE IF EXISTS `work`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `des_name` varchar(20) NOT NULL,
  `work` varchar(100) NOT NULL,
  `work_status` varchar(20) NOT NULL DEFAULT '0',
  `handle_name` varchar(20) DEFAULT NULL,
  `operate` varchar(255) NOT NULL,
  `des_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `handle_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work`
--

LOCK TABLES `work` WRITE;
/*!40000 ALTER TABLE `work` DISABLE KEYS */;
INSERT INTO `work` VALUES (4,'test','db_mod','2','test','modify reboot10 database','2016-10-14 06:54:54','2016-10-16 11:10:31'),(5,'test','db_mod','2','test','modify reboot10 database','2016-10-14 06:54:55','2016-10-16 12:08:05'),(6,'test','db_mod','2','test','modify reboot10 database','2016-10-14 06:54:56','2016-10-16 12:08:09'),(7,'test','db_mod','2','test','modify reboot10 database','2016-10-14 06:54:58','2016-10-16 12:08:13'),(8,'test','db_mod','2','test','modify reboot10 database','2016-10-14 06:54:59','2016-10-16 09:10:37'),(9,'test','db_mod','2','test','modify reboot.user table','2016-10-14 06:56:03','2016-10-16 11:10:47'),(11,'test','user_mod','2','test','modify admin permission','2016-10-14 07:00:32','2016-10-16 12:17:18'),(12,'test','user_mod','2','test','test','2016-10-14 07:01:09','2016-10-16 12:08:52'),(13,'test','user_mod','2','test','test','2016-10-14 07:01:28','2016-10-16 12:08:58'),(14,'test','user_mod','2','test','test','2016-10-14 07:02:16','2016-10-16 12:09:02'),(15,'test','user_mod','2','test','testtest','2016-10-14 07:07:27','2016-10-16 12:09:07'),(17,'test1','web_err','2','test','web error!','2016-10-16 12:17:45','2016-10-16 12:28:57'),(18,'test','user_mod','1','test','modify reboot10 permission','2016-10-16 12:32:17','0000-00-00 00:00:00'),(19,'test1','web_err','0',NULL,'web error!','2016-10-16 12:33:09','0000-00-00 00:00:00'),(20,'admin','db_mod','1','test','modify db','2016-10-16 12:33:53','0000-00-00 00:00:00'),(21,'test','db_mod','1','test','modify db permission','2016-10-16 16:26:10','0000-00-00 00:00:00'),(22,'test','other','0',NULL,'other','2016-10-16 16:26:33','0000-00-00 00:00:00'),(23,'test','user_mod','0',NULL,'test','2016-10-16 16:44:39','0000-00-00 00:00:00'),(24,'test','user_mod','0',NULL,'test','2016-10-16 16:45:02','0000-00-00 00:00:00'),(25,'test','user_mod','0',NULL,'test','2016-10-16 16:46:31','0000-00-00 00:00:00'),(26,'test','db_mod','1','test','haha','2016-10-17 01:04:30','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `work` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-17  9:07:06
