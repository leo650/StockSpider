#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import time,datetime
import json,re

response_jsonp='''jsonpCallback123({"actionErrors":[],"actionMessages":[],"errorMessages":[],"errors":{},"fieldErrors":{},"isPagination":"true","jsonCallBack":"jsonpCallback25686","locale":"zh_CN","pageHelp":{"beginPage":4,"cacheSize":1,"data":[{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"10153","branchsell":"海通证券股份有限公司上海闵行区吴中路证券营业部","branchbuy":"华泰证券股份有限公司上海武定路证券营业部","tradeprice":"2.18","NUM":"76","ifZc":"否","tradeamount":"22133.54","abbrname":"华锐风电"},{"stockid":"601939","tradedate":"2017-01-10","tradeqty":"1361.08","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"5.47","NUM":"77","ifZc":"否","tradeamount":"7445.08","abbrname":"建设银行"},{"stockid":"601818","tradedate":"2017-01-10","tradeqty":"2393.43","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"3.91","NUM":"78","ifZc":"否","tradeamount":"9358.3","abbrname":"光大银行"},{"stockid":"601800","tradedate":"2017-01-10","tradeqty":"252.88","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"15.31","NUM":"79","ifZc":"否","tradeamount":"3871.64","abbrname":"中国交建"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"610.71","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"国都证券股份有限公司北京北三环中路证券营业部","tradeprice":"2.03","NUM":"80","ifZc":"否","tradeamount":"1239.75","abbrname":"华锐风电"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"203.67","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"81","ifZc":"否","tradeamount":"413.46","abbrname":"华锐风电"},{"stockid":"603299","tradedate":"2017-01-10","tradeqty":"28.2","branchsell":"中信建投证券股份有限公司安吉天荒坪路证券营业部","branchbuy":"中信建投证券股份有限公司安吉天荒坪路证券营业部","tradeprice":"14.63","NUM":"82","ifZc":"否","tradeamount":"412.57","abbrname":"井神股份"},{"stockid":"600196","tradedate":"2017-01-10","tradeqty":"30","branchsell":"中国银河证券股份有限公司上海五莲路证券营业部","branchbuy":"中国银河证券股份有限公司上海五莲路证券营业部","tradeprice":"21.1","NUM":"83","ifZc":"否","tradeamount":"633","abbrname":"复星医药"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"84","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"601328","tradedate":"2017-01-10","tradeqty":"4406.48","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"5.79","NUM":"85","ifZc":"否","tradeamount":"25513.51","abbrname":"交通银行"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华安证券股份有限公司大连会展路证券营业部","tradeprice":"2.03","NUM":"86","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"601169","tradedate":"2017-01-10","tradeqty":"1857.47","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"9.86","NUM":"87","ifZc":"否","tradeamount":"18314.7","abbrname":"北京银行"},{"stockid":"600803","tradedate":"2017-01-10","tradeqty":"150","branchsell":"中信建投证券股份有限公司上海市徐家汇路证券营业部","branchbuy":"恒泰证券股份有限公司深圳香林路证券营业部","tradeprice":"14.31","NUM":"88","ifZc":"否","tradeamount":"2146.5","abbrname":"新奥股份"},{"stockid":"600007","tradedate":"2017-01-10","tradeqty":"31.66","branchsell":"东方证券股份有限公司杭州体育场路证券营业部","branchbuy":"广发证券股份有限公司杭州钱江路证券营业部","tradeprice":"15.95","NUM":"89","ifZc":"否","tradeamount":"504.99","abbrname":"中国国贸"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"203.67","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"90","ifZc":"否","tradeamount":"413.46","abbrname":"华锐风电"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"91","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"招商证券股份有限公司北京知春东里证券营业部","tradeprice":"2.03","NUM":"92","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"603166","tradedate":"2017-01-10","tradeqty":"249.38","branchsell":"华泰证券股份有限公司南京中央路第三证券营业部","branchbuy":"中信证券股份有限公司南京高楼门证券营业部","tradeprice":"16.04","NUM":"93","ifZc":"否","tradeamount":"4000.06","abbrname":"福达股份"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"94","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"600466","tradedate":"2017-01-10","tradeqty":"50","branchsell":"中信证券股份有限公司北京东三环中路证券营业部","branchbuy":"长城证券股份有限公司深圳龙岗大道证券营业部","tradeprice":"9.3","NUM":"95","ifZc":"否","tradeamount":"465","abbrname":"蓝光发展"},{"stockid":"600519","tradedate":"2017-01-10","tradeqty":"1.61","branchsell":"华泰证券股份有限公司深圳益田路荣超商务中心证券营业部","branchbuy":"华泰证券股份有限公司深圳益田路荣超商务中心证券营业部","tradeprice":"332","NUM":"96","ifZc":"否","tradeamount":"534.52","abbrname":"贵州茅台"},{"stockid":"603018","tradedate":"2017-01-10","tradeqty":"10.55","branchsell":"国泰君安证券股份有限公司南安成功街证券营业部","branchbuy":"国泰君安证券股份有限公司南京中央路证券营业部","tradeprice":"31.94","NUM":"97","ifZc":"否","tradeamount":"336.97","abbrname":"中设集团"},{"stockid":"600870","tradedate":"2017-01-10","tradeqty":"160","branchsell":"中国银河证券股份有限公司北京建国路证券营业部","branchbuy":"东北证券股份有限公司辽宁分公司","tradeprice":"8.5","NUM":"98","ifZc":"否","tradeamount":"1360","abbrname":"厦华电子"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"305.36","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"99","ifZc":"否","tradeamount":"619.87","abbrname":"华锐风电"},{"stockid":"600180","tradedate":"2017-01-10","tradeqty":"69.18","branchsell":"中国国际金融股份有限公司北京建国门外大街证券营业部","branchbuy":"中信建投证券股份有限公司北京市东直门南大街证券营业部","tradeprice":"13.94","NUM":"100","ifZc":"否","tradeamount":"964.37","abbrname":"瑞茂通"}],"endDate":null,"endPage":41,"objectResult":null,"pageCount":49,"pageNo":4,"pageSize":25,"searchDate":null,"sort":null,"startDate":null,"total":1205},"result":[{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"10153","branchsell":"海通证券股份有限公司上海闵行区吴中路证券营业部","branchbuy":"华泰证券股份有限公司上海武定路证券营业部","tradeprice":"2.18","NUM":"76","ifZc":"否","tradeamount":"22133.54","abbrname":"华锐风电"},{"stockid":"601939","tradedate":"2017-01-10","tradeqty":"1361.08","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"5.47","NUM":"77","ifZc":"否","tradeamount":"7445.08","abbrname":"建设银行"},{"stockid":"601818","tradedate":"2017-01-10","tradeqty":"2393.43","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"3.91","NUM":"78","ifZc":"否","tradeamount":"9358.3","abbrname":"光大银行"},{"stockid":"601800","tradedate":"2017-01-10","tradeqty":"252.88","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"15.31","NUM":"79","ifZc":"否","tradeamount":"3871.64","abbrname":"中国交建"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"610.71","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"国都证券股份有限公司北京北三环中路证券营业部","tradeprice":"2.03","NUM":"80","ifZc":"否","tradeamount":"1239.75","abbrname":"华锐风电"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"203.67","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"81","ifZc":"否","tradeamount":"413.46","abbrname":"华锐风电"},{"stockid":"603299","tradedate":"2017-01-10","tradeqty":"28.2","branchsell":"中信建投证券股份有限公司安吉天荒坪路证券营业部","branchbuy":"中信建投证券股份有限公司安吉天荒坪路证券营业部","tradeprice":"14.63","NUM":"82","ifZc":"否","tradeamount":"412.57","abbrname":"井神股份"},{"stockid":"600196","tradedate":"2017-01-10","tradeqty":"30","branchsell":"中国银河证券股份有限公司上海五莲路证券营业部","branchbuy":"中国银河证券股份有限公司上海五莲路证券营业部","tradeprice":"21.1","NUM":"83","ifZc":"否","tradeamount":"633","abbrname":"复星医药"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"84","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"601328","tradedate":"2017-01-10","tradeqty":"4406.48","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"5.79","NUM":"85","ifZc":"否","tradeamount":"25513.51","abbrname":"交通银行"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华安证券股份有限公司大连会展路证券营业部","tradeprice":"2.03","NUM":"86","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"601169","tradedate":"2017-01-10","tradeqty":"1857.47","branchsell":"瑞银证券有限责任公司上海花园石桥路证券营业部","branchbuy":"瑞银证券有限责任公司上海花园石桥路证券营业部","tradeprice":"9.86","NUM":"87","ifZc":"否","tradeamount":"18314.7","abbrname":"北京银行"},{"stockid":"600803","tradedate":"2017-01-10","tradeqty":"150","branchsell":"中信建投证券股份有限公司上海市徐家汇路证券营业部","branchbuy":"恒泰证券股份有限公司深圳香林路证券营业部","tradeprice":"14.31","NUM":"88","ifZc":"否","tradeamount":"2146.5","abbrname":"新奥股份"},{"stockid":"600007","tradedate":"2017-01-10","tradeqty":"31.66","branchsell":"东方证券股份有限公司杭州体育场路证券营业部","branchbuy":"广发证券股份有限公司杭州钱江路证券营业部","tradeprice":"15.95","NUM":"89","ifZc":"否","tradeamount":"504.99","abbrname":"中国国贸"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"203.67","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"90","ifZc":"否","tradeamount":"413.46","abbrname":"华锐风电"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"91","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"招商证券股份有限公司北京知春东里证券营业部","tradeprice":"2.03","NUM":"92","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"603166","tradedate":"2017-01-10","tradeqty":"249.38","branchsell":"华泰证券股份有限公司南京中央路第三证券营业部","branchbuy":"中信证券股份有限公司南京高楼门证券营业部","tradeprice":"16.04","NUM":"93","ifZc":"否","tradeamount":"4000.06","abbrname":"福达股份"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"101.68","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"94","ifZc":"否","tradeamount":"206.42","abbrname":"华锐风电"},{"stockid":"600466","tradedate":"2017-01-10","tradeqty":"50","branchsell":"中信证券股份有限公司北京东三环中路证券营业部","branchbuy":"长城证券股份有限公司深圳龙岗大道证券营业部","tradeprice":"9.3","NUM":"95","ifZc":"否","tradeamount":"465","abbrname":"蓝光发展"},{"stockid":"600519","tradedate":"2017-01-10","tradeqty":"1.61","branchsell":"华泰证券股份有限公司深圳益田路荣超商务中心证券营业部","branchbuy":"华泰证券股份有限公司深圳益田路荣超商务中心证券营业部","tradeprice":"332","NUM":"96","ifZc":"否","tradeamount":"534.52","abbrname":"贵州茅台"},{"stockid":"603018","tradedate":"2017-01-10","tradeqty":"10.55","branchsell":"国泰君安证券股份有限公司南安成功街证券营业部","branchbuy":"国泰君安证券股份有限公司南京中央路证券营业部","tradeprice":"31.94","NUM":"97","ifZc":"否","tradeamount":"336.97","abbrname":"中设集团"},{"stockid":"600870","tradedate":"2017-01-10","tradeqty":"160","branchsell":"中国银河证券股份有限公司北京建国路证券营业部","branchbuy":"东北证券股份有限公司辽宁分公司","tradeprice":"8.5","NUM":"98","ifZc":"否","tradeamount":"1360","abbrname":"厦华电子"},{"stockid":"601558","tradedate":"2017-01-10","tradeqty":"305.36","branchsell":"华泰证券股份有限公司大连胜利路证券营业部","branchbuy":"华泰证券股份有限公司大连胜利路证券营业部","tradeprice":"2.03","NUM":"99","ifZc":"否","tradeamount":"619.87","abbrname":"华锐风电"},{"stockid":"600180","tradedate":"2017-01-10","tradeqty":"69.18","branchsell":"中国国际金融股份有限公司北京建国门外大街证券营业部","branchbuy":"中信建投证券股份有限公司北京市东直门南大街证券营业部","tradeprice":"13.94","NUM":"100","ifZc":"否","tradeamount":"964.37","abbrname":"瑞茂通"}],"sqlId":"COMMON_SSE_XXPL_JYXXPL_DZJYXX_L_1","texts":null,"type":"","validateCode":""})
'''
# 解析下载的html
# html 下载的html 内容
# pauseDate  上次获取的时间
# isIncreament 是否全量
def parse_html(html,pauseDate='2016-10-01',isIncreament=True):
	return_flag=False
	soup=BeautifulSoup(html,'html.parser')
	all_tr=soup.find_all('tr')
	data_list=[]
	t=time.strptime(pauseDate,"%Y-%m-%d")
	y,m,d=t[0:3]
	pauseD=datetime.datetime(y,m,d)
	for tr in all_tr:
		td_all=tr.find_all('td')
		if return_flag:
			return data_list
		if len(td_all)>1:
			data=()
			for n,td in enumerate(td_all):
				#删除a标签
				if td.a and n==8:
					td.a.decompose()
				#判断是否大于指定的日期
				if isIncreament and n==1:
					t0=time.strptime(td.get_text(),"%Y-%m-%d")
					y0,m0,d0=t0[0:3]
					pauseD0=datetime.datetime(y0,m0,d0)
					if pauseD>pauseD0:
						return_flag=True
						return data_list
				data+=(td.get_text(),)
			data_list.append(data)
	return data_list

# 解析jsonp数据
def parse_jsonp(jsonp_text):
	if len(jsonp_text)<1:
		raise Exception('参数不能为空')
	# 以下解析jsonp 代码
	j=json.loads(re.findall(r'^\w+\((.*)\)$',jsonp_text)[0])
	# 解析数据
	json_data=j['result']
	return json_data
# json 数据清洗，目的是为了统一入库
def elt_json(json_list):
	data_list=[]
	if len(json_list)<1:
		return data_list
	print(len(json_list))
	# deal_date,stock_code,stock_name,stock_price,deal_price,deal_share,deal_amout,deal_rate,deal_buyer,deal_seller,is_special,stock_market,data_from
	for data in json_list:
		print(data['tradedate'])
	return data_list
def main():
	list_data=parse_html(html_content, '2016-12-31',False)
	#print(len(list_data), ...)
	#print(parse_jsonp(response_jsonp))


if __name__=='__main__':
	main()
