# -*- coding: utf-8 -*-

# python模块定义
'''
多个程序段封装为函数, 多个函数封装为模块
函数在类或者模块中叫方法
python自带模块安装在lib目录中
'''

# 模块类别
'''
自带模块
第三方模块
自定义模块, 将自己写的模块放入python lib目录下
'''

# 第三方模块安装方式
'''
pip安装命令行执行
pip install modelename

whl下载安装
pip install path/modelename.whl

直接复制lib目录下的模块目录至对应的lib目录下

anaconda安装
'''

# 模块的导入
import cgi
cgi.closelog()

import numpy
arr = numpy.array([1, 2, 3])
print(arr)

# 使用模块的方法
from cgi import closelog
closelog()

from numpy import array
arr1 = array([2, 3, 4])
print(arr1)

# 将模块中的所有方法导入
from numpy import *
arr2 = array([3, 3, 3])
ones1 = ones([1, 2])
print(arr2)
print(ones1)

