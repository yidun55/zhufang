#coding: utf-8

from scrapy import log
def for_ominated_data(info_list,i_list):
    """
    some elements are ominated, set the ominated elements
    as "" 
    """
    try:
        if len(i_list) == 0:
            i_list.append("")
            i_list.append("")
        else:
            pass
        # assert len(i_list) == 2, "the element must be unique"
        i_list_strip = []
        i_list_strip.append(i_list[0].strip())  #去除两端的/n,/t/r
        info_list.extend(i_list_strip)
        # print 'you work'
        return info_list
    except Exception, e:
        log.msg('i work {m} info = {info}'.format(m=e, info='\001'.join(info_list)), level=log.ERROR)
