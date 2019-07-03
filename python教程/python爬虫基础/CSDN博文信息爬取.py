# -*- coding: utf-8 -*-

import urllib.request
import re
import os


url = 'https://blog.csdn.net/'

# 模拟请求头
headers = (
    'User-Agent',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
)
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 安装为全局
urllib.request.install_opener(opener)

# 开始爬取
data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
pat = '<h2>.*?<a href="(.*?)".*?</h2>'
all_links = re.compile(pat, re.S).findall(data)
print(all_links)
try:
    os.mkdir('download')
except OSError:
    pass
for link in all_links:
    index = all_links.index(link)
    urllib.request.urlretrieve(link, filename='{}/{}.html'.format('download', index))
    print('当前文章第%s篇爬取完成!' % index)
