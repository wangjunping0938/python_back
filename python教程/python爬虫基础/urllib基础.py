# -*- coding: utf-8 -*-

import os
import urllib.request

# urlretrieve(),直接下载网页至本地
try:
    os.mkdir('download')
except OSError:
    pass
urllib.request.urlretrieve('https://cn.bing.com/', 'download/bing.html')

# urlcleanup()清除已经缓存的网页内容
urllib.request.urlcleanup()

# info() 查看爬取情况
file = urllib.request.urlopen('https://cn.bing.com/')
print(file.info())

# getcode()
print(file.getcode())

# geturl() 获取当前访问的url
print(file.geturl())
