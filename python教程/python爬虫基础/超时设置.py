# -*- coding: utf-8 -*-

import urllib.request

for i in range(0, 30):
    try:
        file = urllib.request.urlopen('https://cn.bing.com/', timeout=0.1)
        print(len(file.read().decode('utf-8', 'ignore')))
    except Exception as e:
        print('请求异常', e)
