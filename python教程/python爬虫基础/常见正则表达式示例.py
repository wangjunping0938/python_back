# -*- coding: utf-8 -*-

import re


# 匹配.com和.cn网址
element = '<a href="http://www.baidu.com">百度首页</a>'
pat = '[a-zA-Z]+://[^\s]*[.com|.cn]'
rst = re.compile(pat).findall(element)
print(rst)

# 匹配电话号码
phone ='''jsjsjlaiiwoajkl021-8989829383211928910sjljalkjskluoiwjskjjlks0773-776263626
26363jslajlkj'''
pat = '\d{4}-\d{7}|\d{3}-\d{8}'
rst = re.compile(pat).findall(phone)
print(rst)
