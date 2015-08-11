#coding: utf-8
"""
提取郑州住房信息的xpath语句
"""
xpath_syn_list =[
"//div[@class='list4']/a/@href",   #提取http://bzb.zzfdc.gov.cn/class-1-88.aspx
"//div[@class='list61']/p/a/@href"  #提取http://bzb.zzfdc.gov.cn/article-95-820.aspx
"//div[@class='list61']/h1/text()"   #提取http://bzb.zzfdc.gov.cn/article-95-820.aspx
]