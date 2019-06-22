# -*- coding: utf-8 -*-

import os


# 创建目录
try:
    os.mkdir('folder')
except OSError:
    pass

# 重命名目录
os.rename('folder', 'folder1')

# 遍历目录
print(os.listdir('xlsx'))

#删除目录
os.rmdir('folder')
