# -*- coding: utf-8 -*-

import urllib.request

# 浏览器伪装
# 请求头信息设置
url = 'https://blog.csdn.net/'
headers = (
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
)
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
print(len(data))
