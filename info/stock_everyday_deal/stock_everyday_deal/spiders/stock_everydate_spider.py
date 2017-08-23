import scrapy
from everydate_deal import StockEverydayDealItem

class EveryDateDealSpider(scrapy.Spider):
    name = "everydate_deal"

    def start_requests(self):
        urls = [
            'http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehistory.php?symbol=sh600000&date=2017-04-20&page=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for tr in response.css('table.datatbl tbody tr'):
            item=StockEverydayDealItem()
            item['stock_code']='600000'
            item['stock_name']='浦发银行'
            item['deal_date']='2017-04-20'
            item['deal_time']=tr.css('th::text').extract_first(),
            item['deal_price']=tr.css('td::text')[0].extract(),
            item['ratio']=tr.css('td::text')[1].extract(),
            item['varies']=tr.css('td::text')[2].extract(),
            item['deal_share']=tr.css('td::text')[3].extract(),
            item['deal_amout']=tr.css('td::text')[4].extract(),
            item['deal_type']=tr.css('th')[1].xpath('(./h5|./h6|./h1)/text()').extract_first()
            yield item