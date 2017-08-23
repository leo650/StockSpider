
# import csv
# with open("/Users/leo/trscases/gitproject/StockSpider/info/sz_stock.csv",'r',encoding='gbk') as csvfile:
# 	     read = csv.reader(csvfile)
# 	     for i in read:
# 	     	print(i)
# import requests 
# url = 'http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2' 
# r = requests.get(url) 
# with open("/Users/leo/trscases/gitproject/StockSpider/info/test1_stock.xlsx", "wb") as code:
#      code.write(r.content)
file=open("/Users/leo/trscases/gitproject/StockSpider/info/test_stock.txt",'r',encoding='gbk')
try:
	for line in file:
		if line:
			split_line=line.rstrip('\n').split("\t")
			if(len(split_line)!=10):
				print(split_line, ...)
finally:
	file.close()