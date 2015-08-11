/* 
* @Author: vicvinc
* @Date:   2015-07-20 11:28:48
* @Last Modified by:   Administrator
* @Last Modified time: 2015-07-20 14:05:50
*/

-- ----------------------------
--  Table structure for `panel`
-- ----------------------------
DROP TABLE IF EXISTS `panel`;
CREATE TABLE `panel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20),
  'describe' varchar(40),
  `created` varchar(16),
  `updated` varchar(16),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;