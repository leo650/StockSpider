# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from stock_everytime_deal.items import StockEverytimeDealItem
import scrapy
import datetime

class everytimespider(CSVFeedSpider):
    name='everytimespider'
    delimiter='	'
    quotechar='"'
    #headers=['stock_code','stock_name','deal_date_time','deal_date','deal_time','deal_price','ratio','varies','deal_share','deal_amout','deal_type','data_from']
    headers=['deal_time','deal_price','varies','deal_share','deal_amout','deal_type']
    #start_urls=['http://market.finance.sina.com.cn/downxls.php?date=2017-08-21&symbol=sz000554']
    nowtime=datetime.datetime.now()
    default_n_days=60
    
    
    def start_requests(self):
        #获取所有的代码
        #stock_sql='select stock_code from stock limit 1;'
        stock_sql='select stock_code from stock;'
        self.cur.execute(stock_sql)
        stock_code=[('300105',),('002161',),('002488',),('002431',),('002448',)] 
        #stock_code=self.cur.fetchall()
        #时间参数
        for code in stock_code:
            self.logger.info("type of code:"+str(type(code[0])))
            self.logger.info("code:"+code[0])
            str_code=code[0]
            if str_code.startswith('6'):
                str_code='sh'+str_code
            else:
                str_code='sz'+str_code
            #查询最后的时间
            date_sql="select deal_date from everytime_deal where stock_code="+str(code[0])+" order by deal_date desc limit 1;"
            self.cur.execute(date_sql)
            stock_last_date=self.cur.fetchone()
            #如果第一次获取数据，向前取n天
            if stock_last_date is None:
                self.logger.info("stock_last_date is null!")
                delta_add=datetime.timedelta(days=1)
                delta_sub=datetime.timedelta(days=self.default_n_days)
                nowtime1=self.nowtime-delta_sub
                for i in range(0,self.default_n_days):
                    nowtime1_str=nowtime1.strftime('%Y-%m-%d')
                    nowtime1=nowtime1+delta_add
                    yield scrapy.Request(url='http://market.finance.sina.com.cn/downxls.php?date='+nowtime1_str+'&symbol='+str_code,meta={'date':nowtime1_str,'code':code[0]})
            #之前已经采集过数据的情况
            else:
                self.logger.info("stock_last_date:"+str(stock_last_date[0]))
                start_date=datetime.datetime.strptime(stock_last_date[0].isoformat(),'%Y-%m-%d')
                delta_add=datetime.timedelta(days=1)
                start_date=start_date+delta_add
                while(start_date.date()<self.nowtime.date()):
                    start_date_str=start_date.strftime('%Y-%m-%d')
                    start_date=start_date+delta_add
                    yield scrapy.Request(url='http://market.finance.sina.com.cn/downxls.php?date='+start_date_str+'&symbol='+str_code,meta={'date':start_date_str,'code':code[0]})
       
    
    def adapt_response(self,response):
        #unicode(response.body.decode('gbk')).encode('utf-8')
        #response.text=response.body.decode('gbk')
        return response
    
    def parse_row(self,response,row): 
        #self.logger.info("meta[stock_code]:"+response.meta['code']+";meta[date]:"+response.meta['date'])
        #self.logger.info("url:"+response.url)
        #self.logger.info("isinstance of row:"+str(row['deal_price'].find('.')))
        if row['deal_price'].find('.')>0:
            item = StockEverytimeDealItem()
            item['stock_code'] = response.meta['code']
            item['deal_date'] = response.meta['date']
            item['deal_date_time']=response.meta['date']+" "+row['deal_time']
            #item['stock_name'] = row['stock_name']
            item['deal_time']=row['deal_time']
            item['deal_price']=row['deal_price']
            item['ratio']='0'
            item['varies']=row['varies']
            item['deal_share']=row['deal_share']
            item['deal_amout']=row['deal_amout']
            item['deal_type']=row['deal_type']
            item['data_from']='sina'
            return item
        else:
            pass
    
    def process_results(self, response, results):
        for item in results:
            #item['deal_type']='卖盘'
            if item['varies']=='--':
                item['varies']='0'
            if item['varies']=='价格变动':
                results.remove(item)
            if item['deal_type']=='ÖÐÐÔÅÌ':
                item['deal_type']='中性盘'
            elif item['deal_type']=='ÂòÅÌ':
                item['deal_type']='买盘'
            else:
                item['deal_type']='卖盘'
            #self.logger.info("item:%s",item)
        return results 
       
