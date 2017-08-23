#!/usr/bin/env python
# # _*_ coding:utf-8 _*_
copy_sql='insert into block_deal(deal_date,stock_code,stock_name,deal_price,deal_share,deal_amout,deal_buyer,deal_seller,is_special,stock_price,deal_rate,stock_market,data_from) select deal_date,stock_code,stock_name,deal_price,deal_share,deal_amout,deal_buyer,deal_seller,is_special,stock_price,deal_rate,stock_market,data_from from block_deal_test'
clear_sql='truncate table block_deal_test'
#返回copy sql
def getCopySql():
	return copy_sql

def getClearSql():
	return clear_sql