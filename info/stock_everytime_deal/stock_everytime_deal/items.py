# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockEverytimeDealItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #stock_code VARCHAR(10) NOT NULL comment '交易代码',
    stock_code=scrapy.Field()
    #stock_name VARCHAR(10) NOT NULL comment '代码名称',
    stock_name=scrapy.Field()
    #deal_date_time DATETIME NOT NULL comment '交易的日期及时间',
    deal_date_time=scrapy.Field()
    #deal_date DATE NOT NULL comment '交易日期',
    deal_date=scrapy.Field()
    #deal_time TIME NOT NULL comment '交易时间',
    deal_time=scrapy.Field()
    #deal_price FLOAT NOT NULL comment '成交价格',
    deal_price=scrapy.Field()
    #ratio FLOAT NOT NULL comment '涨跌幅',
    ratio=scrapy.Field()
    #varies FLOAT NOT NULL comment '价格变动',
    varies=scrapy.Field()
    #deal_share INT(10) NOT NULL comment '成交量(手)',
    deal_share=scrapy.Field()
    #deal_amout FLOAT NOT NULL comment '成交额(元)',
    deal_amout=scrapy.Field()
    #deal_type ENUM("买盘","卖盘","中性盘") NOT NULL comment '性质',
    deal_type=scrapy.Field()
    #data_from VARCHAR(100) NOT NULL comment '数据来源：上海交易所（sse）
    data_from=scrapy.Field()
