#coding: utf-8

def xpath_syn_list():
    """
    提取郑州住房信息的xpath语句
    """
    return [
    "//div[@class='list4']/a/@href",   #0提取http://bzb.zzfdc.gov.cn/class-1-88.aspx
    "//div[@class='list61']/p/a/@href",  #1提取http://bzb.zzfdc.gov.cn/article-95-820.aspx
    "//div[@class='list61']/p/a/text()" ,  #2提取http://bzb.zzfdc.gov.cn/article-95-820.aspx
    "//div[@class='list5']/div[@class='p_btns']\
    /span/a/@href",    #3提取http://bzb.zzfdc.gov.cn/class-1-88.aspx
    "//div[@class='list61']/h1/text()"    #4提取http://bzb.zzfdc.gov.cn/article-95-820.aspx   
    ]