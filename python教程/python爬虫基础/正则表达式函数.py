# -*- coding: utf-8 -*-
import re

# 正则表达式函数
# re.match()
# re.search()
# re.sub()

str_a = '''hello python scrapy\n你好python爬虫框架\t\tpip install scrapy,
1029020293 pylat'''

# match函数
pat = 'h.*?y'
rst = re.match(pat, str_a, re.I)
print(rst)

# 全局匹配函数
pat = 'py.*?n'
rst = re.compile(pat).findall(str_a)
print(rst)
