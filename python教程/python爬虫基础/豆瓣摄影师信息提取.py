# -*- coding: utf-8 -*-
import re
from urllib import request


# 豆瓣摄影师信息提取
url = 'https://ypy.douban.com/explore/pger/'
data = request.urlopen(url).read().decode('utf-8')
pat = '<div class="name">\n.*<a.*>(.*)</a>'
rst = re.compile(pat).findall(data)
print(rst)


import os
import xlwt

# 创建excel文件存放目录
try:
    os.makedirs('xlsx')
except OSError:
    pass

wk = xlwt.Workbook()
st = wk.add_sheet('photographer')
st.write(0, 0, 'photographer')
for i in range(len(rst)):
    st.write(i+1, 0, rst[i])
wk.save('xlsx/photographer.xls')
print('摄影师信息存储至excel完毕')
