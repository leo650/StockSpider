CREATE TABLE everydate_deal
    (
        id BIGINT NOT NULL AUTO_INCREMENT,
        stock_code VARCHAR(10) NOT NULL comment '交易代码',
        stock_name VARCHAR(10) NOT NULL comment '代码名称',
        deal_date_time DATETIME NOT NULL comment '交易的日期及时间',
        deal_date DATE NOT NULL comment '交易日期',
        deal_time TIME NOT NULL comment '交易时间',
        deal_price FLOAT NOT NULL comment '成交价格',
        ratio FLOAT NOT NULL comment '涨跌幅',
        varies FLOAT NOT NULL comment '价格变动',
        deal_share INT(10) NOT NULL comment '成交量(手)',
        deal_amout FLOAT NOT NULL comment '成交额(元)',
        deal_type ENUM("买盘","卖盘","中性盘") NOT NULL comment '性质',
        data_from VARCHAR(100) NOT NULL comment '数据来源：上海交易所（sse），深圳交易所(szse)，巨潮资讯(cninfo)，同花顺(tonghuashun)',
        PRIMARY KEY (id),
        INDEX everytimedeal_ix1 (stock_code, deal_date)
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='每天的每一笔交易(由于数据是从网站采集回来的，实际的并不能代表每个人每一笔交易，每三秒显示一次交易)'
