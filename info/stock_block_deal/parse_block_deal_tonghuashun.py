from bs4 import BeautifulSoup
import time,datetime

html_content='''<div class="page-loading" style="display: none;">
        <div class="mask"></div>
        <div class="loading-img"></div>
    </div>
         <table class="m-table J-ajax-table">
		<thead>
			<tr>
			    <th width="40" rowspan="3">序号</th>
			    <th width="95" rowspan="3"  class="cur"><a href="javascript:void(0)" class="J-ajax-a" field="enddate" order="asc">交易日期</a><i class="arr-down"></i></th>
			    <th width="80" rowspan="3" ><a href="javascript:void(0)" class="J-ajax-a" field="stockcode" >股票代码</a><i class="arr-down"></i></th>
			    <th width="80" rowspan="3">股票简称</th>
			    <th width="80" rowspan="3" ><a href="javascript:void(0)" class="J-ajax-a" field="close" >最新价</a><i class="arr-down"></i></th>
			    <th width="80" rowspan="3" ><a href="javascript:void(0)" class="J-ajax-a" field="cjj" >成交价格</a><i class="arr-down"></i></th>
			    <th width="95" rowspan="3" ><a href="javascript:void(0)" class="J-ajax-a" field="cjl" >成交量<br/>（万股）</a><i class="arr-down"></i></th>
			    <th width="80" rowspan="3" ><a href="javascript:void(0)" class="J-ajax-a" field="yjl" >溢价率</a><i class="arr-down"></i></th> 
			    <th rowspan="3" >买方营业部</th>
			    <th rowspan="3" >卖方营业部</th>
			</tr>
		</thead>
		<tbody>
     	         <tr >
            <td>1</td>
            <td class="tr cur">2016-12-30</td>
            <td class="tr"><a href="http://stockpage.10jqka.com.cn/000333/" target="_blank">000333</a></td>
            <td class="tr"><a href="http://stockpage.10jqka.com.cn/000333/" target="_blank" code="hs_000333" class="J_showCanvas">美的集团</a></td>
            <td class="tr c-rise">28.17</td>
            <td class="tr">25.22</td>
            <td class="tr">190.30</td>
            <td class="tr c-fall">-10.47%</td>
            <td class="tl">中国国际金融股份有限公司广州天河路证券营业部<a href="http://www.iwencai.com/regression/result-normal?qs=backtest_datadzjy&query=%E5%A4%A7%E5%AE%97%E4%BA%A4%E6%98%93%E4%B9%B0%E6%96%B9%E8%90%A5%E4%B8%9A%E9%83%A8%E5%8C%85%E5%90%AB%E4%B8%AD%E5%9B%BD%E5%9B%BD%E9%99%85%E9%87%91%E8%9E%8D%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%B9%BF%E5%B7%9E%E5%A4%A9%E6%B2%B3%E8%B7%AF%E8%AF%81%E5%88%B8%E8%90%A5%E4%B8%9A%E9%83%A8%3B%E5%A4%A7%E5%AE%97%E4%BA%A4%E6%98%93%E6%BA%A2%E4%BB%B7%E7%8E%87%E5%A4%A7%E4%BA%8E-12%25%E5%B0%8F%E4%BA%8E-6%25&startDate=20141231&endDate=20161230&daysForSaleStrategy=1,3,5,8,10,15,20,25,30" 
            target="_blank" title="次日上涨概率为61.11%， 平均盈利为-0.08%。收益率最高是持股25日后卖出，收益率为4.16%，成功率为83.33%。" class="m-ques-icon wcUrl">&nbsp;</a></td>
            <td class="tl">中国国际金融股份有限公司宁波扬帆路证券营业部</td>
        </tr>
                  <tr class="even">
            <td>2</td>
            <td class="tr cur">2016-12-29</td>
            <td class="tr"><a href="http://stockpage.10jqka.com.cn/000333/" target="_blank">000333</a></td>
            <td class="tr"><a href="http://stockpage.10jqka.com.cn/000333/" target="_blank" code="hs_000333" class="J_showCanvas">美的集团</a></td>
            <td class="tr c-rise">28.17</td>
            <td class="tr">25.22</td>
            <td class="tr">84.30</td>
            <td class="tr c-fall">-10.47%</td>
            <td class="tl">中国国际金融股份有限公司广州天河路证券营业部<a href="http://www.iwencai.com/regression/result-normal?qs=backtest_datadzjy&query=%E5%A4%A7%E5%AE%97%E4%BA%A4%E6%98%93%E4%B9%B0%E6%96%B9%E8%90%A5%E4%B8%9A%E9%83%A8%E5%8C%85%E5%90%AB%E4%B8%AD%E5%9B%BD%E5%9B%BD%E9%99%85%E9%87%91%E8%9E%8D%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%B9%BF%E5%B7%9E%E5%A4%A9%E6%B2%B3%E8%B7%AF%E8%AF%81%E5%88%B8%E8%90%A5%E4%B8%9A%E9%83%A8%3B%E5%A4%A7%E5%AE%97%E4%BA%A4%E6%98%93%E6%BA%A2%E4%BB%B7%E7%8E%87%E5%A4%A7%E4%BA%8E-12%25%E5%B0%8F%E4%BA%8E-6%25&startDate=20141231&endDate=20161230&daysForSaleStrategy=1,3,5,8,10,15,20,25,30" 
            target="_blank" title="次日上涨概率为61.11%， 平均盈利为-0.08%。收益率最高是持股25日后卖出，收益率为4.16%，成功率为83.33%。" class="m-ques-icon wcUrl">&nbsp;</a></td>
            <td class="tl">中国国际金融股份有限公司宁波扬帆路证券营业部</td>
        </tr>
                 
                 </tbody>
	</table>
			<input type="hidden" id="request" value='{"field":"enddate","order":"desc","page":"1","ajax":"1"}'>
		<input type="hidden" id="baseUrl" value='market/dzjy'>
		<input type="hidden" id="requestQuery" value=''>    <div class="m-page J-ajax-page">
    	&nbsp;<a class="cur" href="javascript:void(0)">1</a>&nbsp;&nbsp;<a class="changePage" page="2" href="javascript:void(0);">2</a>&nbsp;&nbsp;<a class="changePage" page="3" href="javascript:void(0);">3</a>&nbsp;&nbsp;<a class="changePage" page="4" href="javascript:void(0);">4</a>&nbsp;&nbsp;<a class="changePage" page="5" href="javascript:void(0);">5</a>&nbsp;&nbsp;<a class="changePage" page="2" href="javascript:void(0);">下一页</a><a class="changePage" page="123" href="javascript:void(0);">尾页</a><span class="page_info">1/123</span>
    </div>
'''
def parse_html(html,pauseDate,isIncreament=True):
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


def main():
	list_data=parse_html(html_content, '2016-12-30')
	print(len(list_data), ...)


if __name__=='__main__':
	main()
