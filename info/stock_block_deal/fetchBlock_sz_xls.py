#!/usr/bin/env python
# # _*_ coding:utf-8 _*_
##导入相关包和方法环境
import pymysql  as db
import requests 
import datetime
import download_block_deal as df
import operate_excel as op
##下载全量或增量文件
isIncreament=False
now_date=datetime.datetime.now().strftime("%Y-%m-%d")
file_path="/Users/leo/trscases/gitproject/StockSpider/info/stock_block_deal/sz_blockdeal_incr.xlsx"
if not isIncreament:
    file_path="/Users/leo/trscases/gitproject/StockSpider/info/stock_block_deal/sz_blockdeal_all.xlsx"
df.download_block_deal_4_sz(file_path=file_path,txtKsrq='2017-01-10',txtZzrq='2017-10-01')
## 读取文件
# stock_list=op.excel_table_byindex(file=file_path)

# ##获取所有列表并保存到mysql数据库中
# conn=db.connect(host='localhost',user='root',passwd='trsadmin',db='stock',charset='utf8') 
# cursor=conn.cursor()
# sql_mod=' REPLACE INTO block_deal(deal_date,stock_code,stock_name,deal_price,deal_share,deal_amout,deal_buyer,deal_seller,is_special,stock_market,data_from)values'
# sql=sql_mod
# insert_count=1
# #1.深市主板(szmb) 2.中小企业板(szmse) 3.创业板(szcn) 4.沪市主板(shmb) 5.香港主板(hkmb) 6.香港创业板(hkgem) 7. 基金  8.债券 9.其它
# type_market=['1','2','3','4','5','6','7','8','9']
# market_name=['深市主板','中小企业板','创业板','沪市主板','香港主板','香港创业板','基金','债券','其它']
# market_code=['szmb','szmse','szcn','shmb','hkmb','hkgem','fund','bound','other']
# print(len(stock_list), ...)
# for data in stock_list:
#     if insert_count %200==0:
#         if sql.endswith(','):
#             sql=sql[:-1]
#         try:
#             cursor.execute(sql)
#             conn.commit()
#         except:
#             print(sql, ...)
#             conn.rollback()
#             raise Exception('提交失败')
#         sql=sql_mod
#     ##据清洗转成以手为单位
#     deal_amout=str(float(data[4])*100)
#     # 类型判断
#     stock_market='9'
#     if data[1].startswith('6'):
#         stock_market='4'
#     elif data[1].startswith('3'):
#         stock_market='3'
#     elif data[1].startswith('002'):
#         stock_market='2'
#     elif data[1].startswith('000'):
#         stock_market='1'    
#     sql+="('"+data[0]+"', '"+data[1]+"', '"+data[2]+"', '"+data[3]+"', '"+deal_amout+"', '"+data[5]+"', '"+data[6]+"', '"+data[7]+"', '0', '"+stock_market+"','szse'),"
#     insert_count+=1
# if sql.endswith(','):
#     sql=sql[:-1]
# try:
# 	cursor.execute(sql)
# 	conn.commit()
# except:
# 	conn.rollback()
# 	raise Exception('提交失败')
# finally:
# 	conn.close()
# print(insert_count)