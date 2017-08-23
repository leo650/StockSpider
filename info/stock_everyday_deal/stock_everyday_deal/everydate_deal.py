# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockEverydayDealItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #交易代码
    stock_code=scrapy.Field()
    #代码名称
    stock_name=scrapy.Field()
    #交易日期
    deal_date=scrapy.Field()
    #交易时间
    deal_time=scrapy.Field()
    #成交价格
    deal_price=scrapy.Field()
    #涨跌幅
    ratio=scrapy.Field()
    #价格变动
    varies=scrapy.Field()
    #成交量(手)
    deal_share=scrapy.Field()
    #成交额(元)
    deal_amout=scrapy.Field()
    #交易性质
    deal_type=scrapy.Field()
    #数据来源(数据来源：上海交易所（sse），深圳交易所(szse)，巨潮资讯(cninfo)，同花顺(tonghuashun))
    data_from=scrapy.Field()