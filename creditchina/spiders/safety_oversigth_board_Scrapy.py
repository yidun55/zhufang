#coding: utf-8

from scrapy import Spider
from scrapy import Request
from scrapy import log
import urllib, time
from creditchina.xpath_tool.extract_coal import *
from creditchina.xpath_tool.extract_non_coal import *
from creditchina.items import *
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class CreditChina(Spider):
    """
    从信用中国网站上爬取安监局的数据
    """
    name = 'safety'
    start_urls = ['http://www.creditchina.gov.cn/channel_record?t=']
    def __init__(self):
        self.data = {} 
        self.data['sources'] = u'安全监管总局'
        self.data['keyword'] = "."
        self.data['type'] = ''
        self.data['page'] = '1'
        self.url = 'http://www.creditchina.gov.cn/channel_record?t='

    def make_requests_from_url(self,url):
        url = url + str(int(time.time()))
        url = url + '&' + urllib.urlencode(self.data)
        self.url = url 
        return Request(url, callback=self.total_pages)

    def total_pages(self, response):
        """
        抽取总页数
        """
        null = None
        print response.body
        r1_json = eval(response.body)
        total = int(r1_json['totalPageCount'])
        for i in range(1,total+1)[200:210]:
            # print self.data, 'self.data'
            print i, "page_number"
            url = 'http://www.creditchina.gov.cn/channel_record?t='
            self.data['page'] = i
            url = url + str(int(time.time()))
            url = url + '&' + urllib.urlencode(self.data)
            # print url,'url1'
            yield Request(url, callback=self.get_detail,dont_filter=True)

    def get_detail(self, response):
        """
        抽取详细信息的url
        """
        null = None
        r2_json = eval(response.body)
        for el in r2_json['results']:
            url = 'http://www.creditchina.gov.cn/channel_record_detail/{encryStr}#csdetail2'
            # print el ,type(el)
            # print type(r2_json['results'])
            # print el['encryStr'].rstrip(), "el['encryStr'].rstrip()"
            url = url.format(encryStr=el['encryStr'].rstrip())
            # print url
            yield Request(url, callback=self.detail,dont_filter=True)

    def detail(self, response):
        """
        解析详细的信息
        """
        sel = response.selector
        item = CreditchinaItem()
        classi = sel.xpath(u"//strong[text()='所属行业：']\
            //../text()").extract()
        # print classi,"classi"
        if len(classi) == 0:
            item['coal'] = coal_data_extract(response)
            # print item['coal'], 'coal'
        else:
            item['non_coal'] = non_coal_data_extract(response)
            # print item['non_coal']

        yield item










