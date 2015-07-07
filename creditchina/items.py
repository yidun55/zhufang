# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CreditchinaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    coal = Field()
    non_coal = Field()
    def __init__(self):
        """
        将item中的值初始化为空
        """
        Item.__init__(self)
        self['coal'] = ''
        self['non_coal'] = ''
