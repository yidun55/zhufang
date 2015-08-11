#coding: utf-8

from scrapy import Spider
from scrapy import Request
from scrapy import log
from scrapy import Selector
import urllib, time
from creditchina.xpath_tool.extract_coal import *
from creditchina.xpath_tool.extract_non_coal import *
from creditchina.items import *
from creditchina.xpath_tool.xpath_syn_list import xpath_syn_list
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class CreditChina(Spider):
    """
    hack的creditchina的代码,直接抓取郑州市住房网的信息
    """
    name = 'zhengzhou'
    download_delay=1
    start_urls = ['http://bzb.zzfdc.gov.cn/class-1-88.aspx']
    def __init__(self):
        self.filter_set = set()
        self.filter_set.add("http://bzb.zzfdc.gov.cn/class-1-88.aspx")

    def parse(self, response):
        sel = Selector(text=response.body)
        urls = [response.url+"-"+str(i) for i in xrange(2,5)]
        for url in urls:
            if url in urls:
                self.filter_set.add(url)
                yield Request(url, callback=self.detail_url,
                    dont_filter=True)

    def detail_url(self, response):
        """
        抽取含有excel文件url的页面url
        """
        sel = Selector(text=response.body)
        urls = sel.xpath(xpath_syn_list[0]).extract()
        urls = ["http://bzb.zzfdc.gov.cn/" + url for url in urls]
        for url in urls:
            yield Request(url, callback=self.get_detail,dont_filter=True)

    def get_detail(self, response):
        """
        下载excel表
        """
        sel = Selector(text=response.body)
        url = sel.xpath(xpath_syn_list[1])
        url = "http://bzb.zzfdc.gov.cn" + url.split("..")[2]
        file_name = sel.xpath(xpath_syn_list[2])
        file_name = file_name[0] + ".xls"
        excel_item = [(urls, file_name)]
        self.download_xls(excel_item)

    def callbackfunc(self,blocknum, blocksize, totalsize):
        '''回调函数
        @blocknum: 已经下载的数据块
        @blocksize: 数据块的大小
        @totalsize: 远程文件的大小
        '''
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        print "%.2f%%"% percent

    def download_xls(self,url_list):
        """
        url_list = [('文件名','文件url')]
        """
        os.chdir("/home/dyh/data/zhufang/zhengzhou")
        for i in url_list:
            urllib.urlretrieve(i[1], i[0], self.callbackfunc)