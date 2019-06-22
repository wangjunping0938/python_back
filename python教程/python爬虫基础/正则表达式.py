# -*- coding: utf-8 -*-

'''原子
普通字符
非打印字符
原子表
通用字符
'''

import re

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


'''元字符
. 匹配除换行符外的任意一个字符
^ 不在原子表里表示开头,在原子表里表示非
$ 匹配结尾
* 匹配前面的字符0次或多次
? 匹配前面的字符0次或1次
+ 匹配前面字符1次或多次
{n} 前面字符出现n次
{n,} 前面的字符出现至少n次
{n, m} 前面的字符至少出现n次, 最多出现m次
| 模式选择符
() 模式单元
'''

pat = "py...."
rst = re.search(pat, str_a)
print(rst)

pat = "^hell...."
rst = re.search(pat, str_a)
print(rst)

pat = '^h.*o'
rst = re.search(pat, str_a)
print(rst)
