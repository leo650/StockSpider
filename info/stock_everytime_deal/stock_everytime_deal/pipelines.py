# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as db
import logging

logger=logging.getLogger('StockEverytimeDealPipelineLogger')

class StockEverytimeDealPipeline(object):
    collection_name = 'stock_erverytime_item'
    
    def __init__(self,host,db,user,passwd,charset):
        self.host=host
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset
       
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            db=crawler.settings.get('MYSQL_DB','stock'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWD'),
            charset=crawler.settings.get('MYSQL_CHARSET', 'utf-8')
        )
    def open_spider(self, spider):
        self.connect=db.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        self.cur=self.connect.cursor()
        spider.cur=self.cur
       
    
    def close_spider(self, spider):
        self.cur.close()
        self.connect.close()
        
    def process_item(self, item, spider):
        sql="INSERT INTO everytime_deal (stock_code, stock_name, deal_date_time, deal_date, deal_time, deal_price, ratio, varies, deal_share, deal_amout, deal_type, data_from) values ('%s',(select stock_name from stock where stock_code='%s') ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(item['stock_code'],item['stock_code'],item['deal_date_time'],item['deal_date'],item['deal_time'],item['deal_price'],item['ratio'],item['varies'],item['deal_share'],item['deal_amout'],item['deal_type'],item['data_from'])
        print("SQL:"+sql)
        self.cur.execute(sql)
        self.connect.commit()
        return item
    
