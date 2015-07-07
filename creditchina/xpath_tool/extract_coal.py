#coding:utf-8
"""
   从信用中国上提取安监局下煤矿企业的数据
"""
from creditchina.xpath_tool.for_ominated_data import for_ominated_data
def coal_data_extract(response):
    """
    """
    sel = response.selector
    info = []
    name = sel.xpath(u"//strong[text()='煤矿名称：']\
        /../text()").extract()   #煤矿名称
    # print name, 'name'
    info = for_ominated_data(info, name[1:2])
    pro = sel.xpath(u"//strong[text()='企业性质：']\
        /../text()").extract()  #企业性质
    info = for_ominated_data(info, pro[1:2])
    prov = sel.xpath(u"//strong[text()='省份：']\
        /../text()").extract()  #省份
    info = for_ominated_data(info, prov[1:2])
    cap = sel.xpath(u"//strong[text()='生产能力(万t/a)：']\
        /../text()").extract()  #生产能力(万t/a)
    info = for_ominated_data(info, cap[1:2])
    gas_level = sel.xpath(u"//strong[text()='瓦斯等级：']\
        /../text()").extract()  #瓦斯等级
    info = for_ominated_data(info, gas_level[1:2])
    safe_day = sel.xpath(u"//strong[text()='安全生产天数：']\
        /../text()").extract()  #安全生产天数
    info = for_ominated_data(info, safe_day[1:2])
    return "\001".join(info)
