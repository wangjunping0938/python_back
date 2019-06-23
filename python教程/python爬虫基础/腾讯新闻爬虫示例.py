# -*- coding: utf-8 -*-

import re
import json
import urllib.request


headers = (
    'User-Agent',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',)
opener = urllib.request.build_opener()
opener.addheaders = [headers]
pars = 'cid=137&token=d0f13d594edfc180f5bf6b845456f3ea&id=&ext=top&page=0&expIds=&callback=__jp1'
url = 'https://pacaio.match.qq.com/irs/rcd?%s' %pars

data = opener.open(url).read().decode('utf-8', 'ignore')
pat = '"title":"(.*?)"'
rst = re.compile(pat).findall(data)
print(rst)

urlpat = '"url":"(.*?)"'
urls = re.compile(urlpat).findall(data)
print(urls)
