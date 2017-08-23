#! /usr/bin/env python
# _*_ coding:utf-8 _*_
import download_block_deal as dbd
import parse_block_deal_sh as pbds
import insert_db as indb
from datetime import *

# 定义当前时间
now_date=datetime.now()
start_date=now_date
end_date=now_date
going_flag=True
while(going_flag):
	#增加一天
	start_str=start_date.strftime('%Y-%m-%d')
	start_date=start_date+timedelta(days=180)
	end_str=start_date.strftime('%Y-%m-%d')
	if start_date>end_date:
		end_str=end_date.strftime('%Y-%m-%d')
		going_flag=False
	# 获取jsonp 内容
	jsonp_content=dbd.get_html_from_shjys(start_str,end_str)
	print(jsonp_content)
	# 解析jsonp 内容得到json内容
	data_json=pbds.parse_jsonp(jsonp_content)
	#插入数据库
	indb.replace_insert_sh_block_deal(data_json,start_str,end_str)