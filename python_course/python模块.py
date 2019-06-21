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
# 使用模块的方法
cgi.closelog()
from cgi import closelog
closelog()

