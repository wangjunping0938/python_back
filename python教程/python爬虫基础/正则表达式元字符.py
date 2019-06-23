# -*- coding: utf-8 -*-

import re

# 元字符
# . 匹配除换行符外的任意一个字符
# ^ 不在原子表里表示开头,在原子表里表示非
# $ 匹配结尾
# * 匹配前面的字符0次或多次
# ? 匹配前面的字符0次或1次
# + 匹配前面字符1次或多次
# {n} 前面字符出现n次
# {n,} 前面的字符出现至少n次
# {n, m} 前面的字符至少出现n次, 最多出现m次
# | 模式选择符
# () 模式单元

str_a = '''hello python scrapy\n你好python爬虫框架\t\tpip install scrapy,
1029020293 pylat'''

pat = "py...."
rst = re.search(pat, str_a)
print(rst)

pat = "^hell...."
rst = re.search(pat, str_a)
print(rst)

pat = '^h.*o'
rst = re.search(pat, str_a)
print(rst)
