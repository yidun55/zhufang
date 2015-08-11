#coding: utf-8

from scrapy import Spider
from scrapy import Request
from scrapy import log
from scrapy import Selector
import urllib, time
from creditchina.xpath_tool.extract_coal import *
from creditchina.xpath_tool.extract_non_coal import *
from creditchina.items import *
from creditchina.xpath_tool.xpath_for_zhufang import xpath_syn_list
import os
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
        self.xpath_all = xpath_syn_list()   #获得含有xpath语句的列表
        self.filter_set = set()
        self.filter_set.add("http://bzb.zzfdc.gov.cn/class-1-88.aspx")

    def parse(self, response):
        sel = Selector(text=response.body)
        urls = sel.xpath(self.xpath_all[3]).extract()
        urls = list(set(urls))   #去重
        urls = ['http://bzb.zzfdc.gov.cn/'+i for i in urls]
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
        urls = sel.xpath(self.xpath_all[0]).extract()
        urls = ["http://bzb.zzfdc.gov.cn/" + url for url in urls]
        for url in urls[0:1]:
            yield Request(url, callback=self.get_detail,dont_filter=True)

    def get_detail(self, response):
        """
        下载excel表
        """
        sel = Selector(text=response.body)
        urls = sel.xpath(self.xpath_all[1]).extract()
        urls = ["http://bzb.zzfdc.gov.cn" + url.split("..")[2] \
            for url in urls]
        file_name = sel.xpath(self.xpath_all[2]).extract()
        file_head = sel.xpath(self.xpath_all[4]).extract()
        file_name = [file_head[0] +"-"+ name + ".xls" for name in file_name]
        excel_item = zip(file_name, urls)
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
        # os.chdir("E:/DLdata")
        for i in url_list:
            urllib.urlretrieve(i[1], i[0], self.callbackfunc)
