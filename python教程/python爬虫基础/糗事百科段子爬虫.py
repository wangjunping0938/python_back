# -*- coding: utf-8 -*-

import urllib.request
import re


# 模拟请求头
headers = (
    'User-Agent',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
)
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 安装为全局
urllib.request.install_opener(opener)

# 构造网址开始爬取
for i in range(0, 35):
    url = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    content = re.compile(pat, re.S).findall(data)
    for c in content:
        print(c)
        print('-'*80)
