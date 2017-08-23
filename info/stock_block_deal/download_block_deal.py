import requests 
import datetime
from urllib.request import Request
from urllib.request import urlopen

## isIncreament 是否增量
## txtKsrq 开始日期（格式 2016-01-01）
## txtZzrq 终止日期（格式 2016-10-01）
## file_path 保存的文件名称
def download_block_deal_4_sz(txtKsrq='',txtZzrq='',file_path='/Users/leo/trscases/gitproject/StockSpider/info/stock_block_deal/sz_blockdeal_incr.xlsx'):
	## 定义相关参数
	if len(txtKsrq)<8:
		txtKsrq=datetime.datetime.now().strftime("%Y-%m-%d")
	if len(txtZzrq)<8:
		txtZzrq=datetime.datetime.now().strftime("%Y-%m-%d")
	url='http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1265_xyjy&tab1PAGENUM=1&ENCODE=1&TABKEY=tab1&txtKsrq='+txtKsrq+'&txtZzrq='+txtZzrq
	##写入文件中
	r = requests.get(url) 
	with open(file_path, "wb") as code:
	      code.write(r.content)
## 从上海交易所获取 jsonp 文件
## startDate 开始日期（格式 2016-01-01）
## endDate  终止日期（格式 2016-10-01）
def get_html_from_shjys(startDate='',endDate=''):
	baseUrl='http://query.sse.com.cn/commonQuery.do?&jsonCallBack=jsonpCallback4255&sqlId=COMMON_SSE_XXPL_JYXXPL_DZJYXX_L_1&stockId=&startDate='+startDate+'&endDate='+endDate+'&pageHelp.beginPage=1&pageHelp.cacheSize=1&_=1484464350728'
	##增加headers
	header={"Cookie":'PHPStat_First_Time_10000011=1482581389559; PHPStat_Cookie_Global_User_Id=_ck16122420094915743552475296553;PHPStat_Return_Time_10000011=1482581389559; PHPStat_Main_Website_10000011=_ck16122420094915743552475296553%7C10000011%7C%7C%7C',
	"Referer":'http://www.sse.com.cn/disclosure/diclosure/block/deal/',
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
	"Host":'query.sse.com.cn'}
	req=Request(baseUrl,None,header)
	##获取所有信息列表
	resp=urlopen(req)
	jsonp_content=resp.read().decode('utf-8')
	return jsonp_content
##从同花顺页面获取html数据
##pagenum 获取的页码
def get_html_from_tonghuashun(pagenum=1):
	baseUrl='http://data.10jqka.com.cn/market/dzjy/field/enddate/order/desc/page/'+str(pagenum)+'/ajax/1/'
	##增加headers
	header={"Cookie":'"Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1483349277,1483362735; spversion=20130314; Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1483349290,1483353916,1483362738; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1483349290,1483353916,1483362736"',
	"Referer":'http://data.10jqka.com.cn/market/dzjy/',
	"Host":'data.10jqka.com.cn'}
	req=Request(baseUrl,None,header)
	##获取所有信息列表
	resp=urlopen(req)
	html_content=resp.read().decode('gbk')
	return html_content

def main():
	print(get_html_from_tonghuashun())
	#print(get_html_from_shjys('2016-10-01','2016-12-30'))

if __name__=='__main__':
	main()