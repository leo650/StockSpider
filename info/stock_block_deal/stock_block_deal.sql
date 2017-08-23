CREATE TABLE `block_deal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deal_date` date NOT NULL COMMENT '交易日期',
  `stock_code` varchar(10) NOT NULL COMMENT '证券代码',
  `stock_name` varchar(10) NOT NULL COMMENT '证券简称',
  `deal_price` float(7,4) NOT NULL COMMENT '成交价格',
  `deal_share` float(16,2) NOT NULL COMMENT '成交量（手）',
  `deal_amout` float(16,2) NOT NULL COMMENT '成交金额（万元）',
  `deal_buyer` varchar(500) NOT NULL COMMENT '买方营业部',
  `deal_seller` varchar(500) NOT NULL COMMENT '卖方营业部',
  `is_special` tinyint(2) NOT NULL COMMENT '是否专场',
  `stock_price` float(7,4) DEFAULT NULL COMMENT '当天收盘价格',
  `deal_rate` float(5,2) DEFAULT NULL COMMENT '溢价或折价比例',
  `stock_market` smallint(3) NOT NULL COMMENT '1.深市主板(szmb) 2.中小企业板(szmse) 3.创业板(szcn) 4.沪市主板(shmb) 5.香港主板(hkmb) 6.香港创业板(hkgem) 7. 基金  8.债券 9.其它 ',
  `data_from` varchar(100) NOT NULL COMMENT '数据来源：上海交易所（sse），深圳交易所(szse)，巨潮资讯(cninfo)，同花顺(tonghuashun)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=144447 DEFAULT CHARSET=utf8