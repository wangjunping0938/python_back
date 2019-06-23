# -*- coding: utf-8 -*-
import re

# 贪婪模式尽可能多的匹配,
# 懒惰模式尽可能少的匹配

str_a = 'pythonyyy'
pat = 'p.*y'  # 贪婪模式匹配,模糊匹配
pat1 = 'p.*?y'  # 懒惰模式,精准匹配
rst1 = re.search(pat, str_a, re.I)
rst2 = re.search(pat1, str_a, re.I)
print(rst1)
print(rst2)
