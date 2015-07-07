#coding: utf-8
"""
  从信用中国上抓取安监局下的非煤矿企业的数据
"""
from creditchina.xpath_tool.for_ominated_data import for_ominated_data
def non_coal_data_extract(response):
    """
    """
    sel = response.selector
    info = []
    name = sel.xpath(u"//strong[text()='企业名称：']\
        /../text()").extract()   #企业名称
    info = for_ominated_data(info, name[1:2])
    # print name[1], "name"
    classi = sel.xpath(u"//strong[text()='所属行业：']\
    //../text()").extract() #所属行业
    info = for_ominated_data(info, classi[2:3])
    safe_le = sel.xpath(u"//strong[text()='安全生产标准化级别：']\
    //../text()").extract() #安全生产标准化级别
    info = for_ominated_data(info, safe_le[2:3])
    type_l = sel.xpath(u"//strong[text()='类型：']\
    //../text()").extract() #类型
    info = for_ominated_data(info, type_l[2:3])
    pub_date = sel.xpath(u"//strong[text()='公告时间：']\
        //../text()").extract()  #公告时间
    info = for_ominated_data(info, pub_date[2:3])
    prov = sel.xpath(u"//strong[text()='所在省份：']\
        /../text()").extract() #省份
    info = for_ominated_data(info, prov[1:2])
    info_re = "\001".join(info)
    if info_re:
        pass     #如果有内容则pass，没有内容则记录下该页面的url
    else:
        log.msg("error in extract_non_coal %s" %response.url,\
            level=log.ERROR)
    return info_re

