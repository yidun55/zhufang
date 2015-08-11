# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
import os
os.chdir("/home/dyh/data/zhufang/zhengzhou")
class CreditchinaPipeline(object):
    def process_item(self, item, spider):
        # f = open("creditchina_coal","a")
        log.msg("pipeline work%s" %("".join(item.values())),\
            level=log.INFO)
        if item['coal']:
            # print 'pipeline coal'
            f = open("creditchina_coal", "a")
            f.write(item['coal']+"\n")
            f.close()
        elif item['non_coal']:
            # print 'pipeline non_coal'
            f = open('creditchina_non_coal', "a")
            f.write(item['non_coal']+"\n")
            f.close()
        else:
            print 'pipeline else'
            log.msg("error in pipeline nothing be extracted")
