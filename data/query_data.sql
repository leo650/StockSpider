select deal_date from everytime_deal where stock_code='000554' order by deal_date desc limit 1;
select distinct(deal_date) from everytime_deal where stock_code='300141' order by deal_date desc;
select * from everytime_deal  where stock_code='000002' and deal_date='2017-08-09'；
select * from everytime_deal where stock_code='002492' order by deal_date desc;