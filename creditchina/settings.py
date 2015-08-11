# -*- coding: utf-8 -*-

# Scrapy settings for creditchina project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'creditchina'

SPIDER_MODULES = ['creditchina.spiders']
NEWSPIDER_MODULE = 'creditchina.spiders'

DEFAULT_ITEM_CLASS='creditchina.items.CreditchinaItem'
ITEM_PIPELINES=['creditchina.pipelines.CreditchinaPipeline']



#LOG_FILE = 'E:/DLdata/log'
LOG_FILE = '/home/dyh/data/zhufang/zhengzhou/log'


DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'creditchina.rotate_useragent.RotateUserAgentMiddleware' :400
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'creditchina (+http://www.yourdomain.com)'
