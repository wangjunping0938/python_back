# -*- coding: utf-8 -*-

import urllib.request
import re
import random


user_agent_pools = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
]

def user_agent(user_agent_pools):
    ua = random.choice(user_agent_pools)
    print(ua)
    headers = ('User-Agent', ua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 安装为全局
    urllib.request.install_opener(opener)


# 使用随机用户代理爬取糗事百科
# 构造网址开始爬取
for i in range(0, 35):
    user_agent(user_agent_pools)
    url = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    content = re.compile(pat, re.S).findall(data)
    for c in content:
        print(c)
        print('-'*80)
