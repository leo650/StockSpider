#!/usr/bin/env python
# # _*_ coding:utf-8 _*_
##导入相关包和方法环境
import pymysql  as db
import datetime
import json

def replace_insert_sh_block_deal(data_json,startDate='',endDate=''):
    if len(data_json)<1:
        print('没有可以插入的数据')
        return
    ##获取同花顺html
    now_date=datetime.datetime.now().strftime("%Y-%m-%d")
    if len(startDate)<2:
        startDate=now_date
    if len(endDate)<2:
        endDate=now_date
    ##获取所有列表并保存到mysql数据库中
    conn=db.connect(host='localhost',user='root',passwd='trsadmin',db='stock',charset='utf8') 
    cursor=conn.cursor()
    #先删除有关的数据
    sql_delete="delete from block_deal_test where data_from='sse' and deal_date>='"+startDate+"' and deal_date<='"+endDate+"'"
    try:
        cursor.execute(sql_delete)
        conn.commit()
    except:
        print(sql_delete, ...)
        conn.rollback()
        raise Exception('删除指定数据失败')
    ##插入数据
    sql_mod=' REPLACE INTO block_deal_test(deal_date,stock_code,stock_name,stock_price,deal_price,deal_share,deal_amout,deal_rate,deal_buyer,deal_seller,is_special,stock_market,data_from)values'
    sql=sql_mod
    insert_count=1
    #1.深市主板(szmb) 2.中小企业板(szmse) 3.创业板(szcn) 4.沪市主板(shmb) 5.香港主板(hkmb) 6.香港创业板(hkgem) 7. 基金  8.债券 9.其它
    type_market=['1','2','3','4','5','6','7','8','9']
    market_name=['深市主板','中小企业板','创业板','沪市主板','香港主板','香港创业板','基金','债券','其它']
    market_code=['szmb','szmse','szcn','shmb','hkmb','hkgem','fund','bound','other']
    print(len(data_json), ...)
    for data in data_json:
        if insert_count %300==0:
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
        deal_share=str(float(data['tradeqty'])*100)
        # 类型判断
        stock_market='4' 
        # %的处理
        is_special='0' if(data['ifZc']=='否') else '1'
        # deal_date,stock_code,stock_name,stock_price,deal_price,deal_share,deal_amout,deal_rate,deal_buyer,deal_seller,is_special,stock_market,data_from
        sql+="('"+data['tradedate']+"', '"+str(data['stockid'])+"', '"+data['abbrname']+"', '0', '"+str(data['tradeprice'])+"', '"+deal_share+"','"+str(data['tradeamount'])+"', '0', '"+data['branchbuy']+"', '"+data['branchsell']+"','"+is_special+"', '"+stock_market+"','sse'),"
        insert_count+=1
    if sql.endswith(','):
        sql=sql[:-1]
    try:
    	cursor.execute(sql)
    	conn.commit()
    except:
    	conn.rollback()
    	raise Exception('提交失败')
    finally:
    	conn.close()
    print(insert_count)