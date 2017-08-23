#!/usr/bin/env python
# # _*_ coding:utf-8 _*_
##导入相关包和方法环境
import pymysql  as db
import requests 
import datetime
## 定义相关参数

url='http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2'
##增加headers
header={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
"Referer":'http://www.szse.cn/main/marketdata/jypz/colist/',
"Host":'www.szse.cn'}
##req=Request(baseUrl,None,header)

##获取所有信息列表
##写入文件中
r = requests.get(url) 
with open("/Users/leo/trscases/gitproject/StockSpider/info/stock_code/sz_stock.xlsx", "wb") as code:
      code.write(r.content)
## 读取文件
file=open('/Users/leo/trscases/gitproject/StockSpider/info/stock_code/sz_stock.txt','r',encoding='gbk')
stock_list=[]
first_line=True
#1.深市主板(szmb) 2.中小企业板(szmse) 3.创业板(szcn) 4.沪市主板(shmb) 5.香港主板(hkmb) 6.香港创业板(hkgem) 
type_market=['1','2','3']
market_name=['深市主板','中小企业板','创业板']
market_code=['szmb','szmse','szcn']
now_date=datetime.datetime.now().strftime("%Y-%m-%d")
try:
    for line in file:
    	if line:
    		market_index=0
    		if first_line:
    			first_line=False
    		else:
    			infos=line.rstrip('\n').split('\t')
    			##数据清洗
    			# 1.市场代码索引确定
    			if infos[0].startswith('3'):
    				market_index=2
    			elif infos[0].startswith('002'):
    				market_index=1
    			# 2.股本数目转成手计算
    			infos[8]=str(int(infos[8].replace(',', ''))/100.0)
    			infos[9]=str(int(infos[9].replace(',', ''))/100.0)
    			infos[13]=str(int(infos[13].replace(',', ''))/100.0)
    			infos[14]=str(int(infos[14].replace(',', ''))/100.0)

    			# 3. 日期转换
    			if len(infos[7])<4:
    				infos[7]=now_date
    			if len(infos[12])<4:
    				infos[12]=now_date
    			#加入列表中
    			stock_list.append((infos[0].strip(),infos[1].strip(),infos[2].strip(),infos[3],infos[4],infos[5].strip(),infos[6].strip(),infos[7].strip(),infos[8].strip(),infos[9].strip(),infos[10],infos[11],infos[12],infos[13],infos[14],infos[15],infos[16],infos[17],infos[18],infos[19],type_market[market_index],market_code[market_index],market_name[market_index],'szse'))
# 	    	    ##'1.公司代码', '2.公司简称', '3.公司全称', '4.英文名称', '5.注册地址', '6.A股代码', '7.A股简称', '8.A股上市日期', '9.A股总股本',
                # '10.A股流通股本', '11.B股代码', '12.B股简称', '13.B股上市日期', '14.B股总股本', '15.B股流通股本', '16.地区', '17.省份', '18.城市', '19.所属行业', '20.公司网址'
finally:
	file.close()
print(len(stock_list), ...)
##获取所有列表并保存到mysql数据库中
conn=db.connect(host='localhost',user='root',passwd='trsadmin',db='stock',charset='utf8') 
cursor=conn.cursor()
sql_mod=' REPLACE INTO stock(company_id,company_name,company_full_name,company_english_name,company_reg_addr,stock_code,stock_name,stock_start_date, stock_total_share, stock_share_circulate,stock_code_B,stock_name_B,stock_start_date_B, stock_total_share_B, stock_share_circulate_B,company_belong_area,company_belong_province,company_belong_city,company_belong_industry,company_website,stock_market,stock_market_code,stock_market_name,data_from)values'
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
	sql+="('"+data[0]+"', '"+data[1]+"', '"+data[2]+"', '"+data[3]+"', '"+data[4]+"', '"+data[5]+"', '"+data[6]+"', '"+data[7]+"', '"+data[8]+"', '"+data[9]+"', '"+data[10]+"', '"+data[11]+"','"+data[12]+"', '"+data[13]+"', '"+data[14]+"', '"+data[15]+"', '"+data[16]+"', '"+data[17]+"', '"+data[18]+"', '"+data[19]+"', '"+data[20]+"', '"+data[21]+"', '"+data[22]+"','"+data[23]+"'),"
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