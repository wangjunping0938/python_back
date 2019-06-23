# -*- coding: utf-8 -*-

import re
import urllib.request

url = 'https://www.csdn.net/'
data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)
# 提取文章ID
pat = 'https?:.*details/(\d*)'
rst = re.compile(pat).findall(data)
print(rst)
