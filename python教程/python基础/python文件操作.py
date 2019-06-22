# -*- coding: utf-8 -*-

# 使用python对文件进行打开, 关闭, 读取, 写入等操作

# open(文件地址, 操作形式)
'''操作形式
w: 写入
r: 读取
b: 二进制
a: 追加
'''

# 打开文件
fh = open('文本1.txt', 'r')
# 读取全部
print(fh.read())
# 单行读取
print(fh.readline())
# 关闭文件
fh.close()

# 文件替换写入
data = '测试内容\n'
fh = open('文本1.txt', 'w')
fh.write(data)
fh.close()

# 追加写入
data = '测试内容1\n'
fh = open('文本1.txt', 'a+')
fh.write(data)
fh.close()


# 文件复制
import shutil

souce_path = 'xlsx/merge.xls'
destination_path = '/tmp/merge.xls'

shutil.copy(souce_path, destination_path)

# 文件删除,重命名
import os
shutil.copy('xlsx/merge.xls', 'merge1.xls')
os.rename('merge1.xls', 'merge2.xls')
os.remove('merge2.xls')
