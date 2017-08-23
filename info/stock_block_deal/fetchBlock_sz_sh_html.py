#!/usr/bin/env python
# # _*_ coding:utf-8 _*_
##导入相关包和方法环境
import pymysql  as db
import requests 
import datetime
import download_block_deal as df
import parse_block_deal_tonghuashun as pbdt
import SysCons as scon
##获取同花顺html
#now_date=datetime.datetime.now().strftime("%Y-%m-%d")
now_date='2017-04-19'
stock_list=[]
going_flag=True
page_curr=1
while going_flag:
    html_content=df.get_html_from_tonghuashun(page_curr)
    #解析数据
    list_data=pbdt.parse_html(html_content,now_date)
    if len(list_data)==0:
        going_flag=False
    else:
        stock_list+=list_data
    page_curr+=1
print(len(stock_list), ...)
##获取所有列表并保存到mysql数据库中
conn=db.connect(host='localhost',user='root',passwd='trsadmin',db='stock',charset='utf8') 
cursor=conn.cursor()
#先删除有关的数据
sql_delete="delete from block_deal where data_from='tonghuashun' and deal_date>='"+now_date+"'"
#sql_delete_test="delete from block_deal_test where data_from='tonghuashun' and deal_date>='"+now_date+"'"
try:
    cursor.execute(sql_delete)
    #cursor.execute(sql_delete_test)
    conn.commit()
except:
    print(sql_delete, ...)
    conn.rollback()
    raise Exception('删除指定数据失败')
##插入数据
sql_mod='INSERT INTO block_deal(deal_date,stock_code,stock_name,stock_price,deal_price,deal_share,deal_amout,deal_rate,deal_buyer,deal_seller,is_special,stock_market,data_from)values'
sql=sql_mod
insert_count=1
#1.深市主板(szmb) 2.中小企业板(szmse) 3.创业板(szcn) 4.沪市主板(shmb) 5.香港主板(hkmb) 6.香港创业板(hkgem) 7. 基金  8.债券 9.其它
type_market=['1','2','3','4','5','6','7','8','9']
market_name=['深市主板','中小企业板','创业板','沪市主板','香港主板','香港创业板','基金','债券','其它']
market_code=['szmb','szmse','szcn','shmb','hkmb','hkgem','fund','bound','other']
print(len(stock_list), ...)
for data in stock_list:
    if insert_count %3==0:
        if sql.endswith(','):
            sql=sql[:-1]
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            print(sql, ...)
            conn.rollback()
            raise Exception('提交失败')
        sql=sql_mod
    ##据清洗转成以手为单位
    deal_amout='%.2f' % (float(data[5])*float(data[6]))
    deal_share=str(float(data[6])*100)
    # 类型判断
    stock_market='9'
    if data[2].startswith('6'):
        stock_market='4'
    elif data[2].startswith('3'):
        stock_market='3'
    elif data[2].startswith('002'):
        stock_market='2'
    elif data[2].startswith('000'):
        stock_market='1'  
    # %的处理
    deal_rate=data[7][:-1]
    # deal_date,stock_code,stock_name,stock_price,deal_price,deal_share,deal_amout,deal_rate,deal_buyer,deal_seller,is_special,stock_market,data_from
    sql+="('"+data[1]+"', '"+data[2]+"', '"+data[3]+"', '"+data[4]+"', '"+data[5]+"', '"+deal_share+"','"+deal_amout+"', '"+deal_rate+"', '"+data[8]+"', '"+data[9]+"', '0', '"+stock_market+"','tonghuashun'),"
    insert_count+=1
if sql.endswith(','):
    sql=sql[:-1]
try:
    cursor.execute(sql)
    conn.commit()
    # copy records to block_deal
    #cursor.execute(scon.getCopySql())
    #conn.commit()
    # clear records in the test db
    #cursor.execute(scon.getClearSql())
    #conn.commit()
except:
    print(sql, ...)
    conn.rollback()
    raise Exception('提交失败')
# try:
#     # copy records to block_deal
#     cursor.execute(scon.getCopySql())
#     conn.commit()
# except:  
#     conn.rollback()
#     raise Exception('copy 失败！')
# try:
#     # clear records in the test db
#     cursor.execute(scon.getClearSql())
#     conn.commit()
# except:
#     conn.rollback()
#     raise Exception('clear 失败！')
# finally:
# 	conn.close()
print(insert_count)