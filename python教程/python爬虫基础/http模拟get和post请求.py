# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib.parse

# get请求实现bing自动搜索
keyword = 'python'
keyword = urllib.request.quote(keyword)
url = 'https://cn.bing.com/search?q={}'.format(keyword)
data = urllib.request.urlopen(url).read().decode('utf-8')
print(len(data))

# post请求
post_url = 'http://www.example.com/login'
post_data = urllib.parse.urlencode({'name':'username', 'passwd':'mypassword'}).encode('utf-8')
req = urllib.request.Request(post_url, post_data)
rst = urllib.request.urlopen(req).read().decode('utf-8')
print(rst)
