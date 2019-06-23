# -*- coding: utf-8 -*-

# URLError
# 1. 无法连接服务器
# 2. 远程url不存在
# 3. 网络未连接
# 4. 触发HTTPError

# HTTPError

import urllib.request
import urllib.error

try:
    data = urllib.request.urlopen('https://blog.csdn.net/').read().decode('utf-8')
    print(len(data))
except urllib.error.URLError as e:
    if hasattr (e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
