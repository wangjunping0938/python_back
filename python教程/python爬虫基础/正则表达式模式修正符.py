# -*- coding: utf-8 -*-

import re

# 模式修正符
# I 忽略大小写
# M 多行匹配
# L 本地化识别匹配
# U Unicode字符编码
# S 让.匹配包括换行符

str_a = '''hello python scrapy\n你好python爬虫框架\t\tpip install scrapy,
1029020293 pylat'''

pat = 'pyt'
rst = re.search(pat, str_a, re.I)
print(rst)


