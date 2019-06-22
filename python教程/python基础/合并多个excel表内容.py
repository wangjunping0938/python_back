# -*- coding: utf-8 -*-

import os
import xlwt
import string
import random
import datetime
import time


# 先生成多个excel文件
# 创建excel文件存放目录
try:
    os.makedirs('xlsx')
except OSError:
    pass

# 表头
titles = ['姓名', '年龄', '性别', '日期', '时间', '薪资']


# 随机生成数据
def random_data():
    name_str = string.ascii_letters
    name = ''.join(random.sample(name_str, random.randint(3, 8)))
    age = random.randint(20, 35)
    sex = random.choice(['男', '女'])
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    hour = time.strftime('%I:%M:%S')
    salary = random.randint(5000, 25000)
    return name, age, sex, date, hour, salary


# 生成随机个数的二维列表
def random_list(number):
    rows = []
    for i in range(number):
        rows.append(random_data())
    return rows


# 数据写入excel文件
def write_excel(titles, rows, filename):
    wk = xlwt.Workbook()  # 新建excel对象
    st = wk.add_sheet('worker')  # 添加名为worker的sheet页
    for i in range(len(titles)):
        st.write(0, i, titles[i])  # 0表示行号, i表示列号, 第3个参数表示值
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            st.write(i+1, j, rows[i][j])
    wk.save(filename)

# 生成随机个文件
for i in range(random.randint(3, 9)):
    filename = '{}/{}.xls'.format('xlsx', 'test{}'.format(i))
    if os.path.exists(filename):
        continue
    rows = random_list(random.randint(5, 10))
    write_excel(titles, rows, filename)
    print('随机excel文件%s生成完成' %filename)


# 多个excel表格合并为一个
import pandas
import numpy
import glob

file_array = []
for fn in glob.glob('xlsx/*.xls'):
    file_array.append(fn)
res = pandas.read_excel(file_array[0])
for i in range(1, len(file_array)):
    r = pandas.read_excel(file_array[i])
    res = pandas.concat([res, r], ignore_index=True)
# 将多个文件合并的内容写入一个文件
writer = pandas.ExcelWriter('xlsx/merge.xls')
res.to_excel(writer, 'worker1')
writer.save()
print('合并完成')
