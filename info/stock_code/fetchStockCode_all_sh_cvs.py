#!/usr/bin/env python
# # _*_ coding:utf-8 _*_
##导入相关包和方法环境
from urllib.request import Request
from urllib.request import urlopen
import pymysql  as db
import datetime
## 定义相关参数

baseUrl='http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1'
##增加headers
header={"Cookie":'PHPStat_First_Time_10000011=1482418270120; PHPStat_Cookie_Global_User_Id=_ck16122222511011335893857616732; PHPStat_Return_Time_10000011=1482665695699; PHPStat_Main_Website_10000011=_ck16122222511011335893857616732%7C10000011%7C%7C%7C;PHPStat_Return_Count_10000011=1',
"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
"Referer":'http://www.sse.com.cn/assortment/stock/list/share/',
"Host":'query.sse.com.cn'}
req=Request(baseUrl,None,header)

##获取所有信息列表
resp=urlopen(req)
doc_content=resp.read().decode('gbk')
##写入文件中
file=open('/Users/leo/trscases/gitproject/StockSpider/info/stock_code/sh_stock.csv','w',encoding='gbk')
file.write(doc_content)
file.close()
## 读取文件
file=open('/Users/leo/trscases/gitproject/StockSpider/info/stock_code/sh_stock.csv',encoding='gbk')
stock_list=[]
first_line=True
nowtimestr=datetime.datetime.now().strftime("%Y-%m-%d")
try:
    for line in file:
    	if line:
	    	if first_line:
	    		first_line=False
	    	else:
	    	    infos=line.split('\t')
	    	    ##清洗数据
	    	    # 1.股本数以手计算
	    	    infos[5]=str(int((float(infos[5].strip()))*100))
	    	    infos[6]=str(int((float(infos[6].strip()))*100))
	    	    # 2.处理没有发行时间的新股
	    	    if len(infos[4])<4:
	    	    	infos[4]=nowtimestr
	    	    stock_list.append((infos[0].strip(),infos[1].strip(),infos[2].strip(),infos[3].strip(),infos[4].strip(),infos[5],infos[6],'4','shmb','沪市主板'))
finally:
	file.close()
##获取所有列表并保存到mysql数据库中
conn=db.connect(host='localhost',user='root',passwd='trsadmin',db='stock',charset='utf8') 
cursor=conn.cursor()
sql_mod=' REPLACE INTO stock(company_id,company_name,stock_code,stock_name,stock_start_date,stock_total_share,stock_share_circulate,stock_market,stock_market_code,stock_market_name,data_from) values'
sql=sql_mod
insert_count=1
for data in stock_list:
	if insert_count %2==0:
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
	sql+="('"+data[0]+"', '"+data[1]+"', '"+data[2]+"', '"+data[3]+"', '"+data[4]+"', '"+data[5]+"', '"+data[6]+"', '"+data[7]+"', '"+data[8]+"', '"+data[9]+"','sse'),"
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
