# -*- coding: utf-8 -*-

import re


# 原子
# 普通字符
# 非打印字符
# 原子表
# 通用字符

str_a = '''hello python scrapy\n你好python爬虫框架\t\tpip install scrapy,
1029020293 pylat'''
print(str_a)

# 普通字符做原子
pat = 'tho'
rst = re.search(pat, str_a)
print(rst)

# 非打印字符做原子
pat = '\n'
rst = re.search(pat, str_a)
print(rst)

# 通用字符做原子
# \w: 匹配 A-Z, a-z, 0-9 _
# \W: 匹配除去A-Z, a-z 0-9 _外的字符
# \d: 十进制数字
# \D：除十进制数字以外的数字
# \s: 空白字符
# \S: 除空白字符外的字符
pat = '\w\d\s\d\d'
rst = re.search(pat, str_a)
print(rst)

# 原子表
pat = 'py[^th]'
rst = re.search(pat, str_a)
print(rst)
