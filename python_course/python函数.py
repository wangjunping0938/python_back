# -*- coding: utf-8 -*-

# 函数本质就是功能的封装, 提高效率和可读性

# 局部变量与全局变量
# 变量的作用域从开始到程序结束都生效叫全局变量
# 变量的作用域只在局部生效叫局部变量

# 全局变量
variable = 100

# 局部变量
def function():
    number = 10
    return number

# 函数定义与参数的使用, 定义时使用的是形参
def function_name(parameter):
    print(parameter)

# 调用函数使用的实参
function_name('hello')

# 比较大小函数
def function2(a, b):
    if a > b:
        print('a大于b')
    elif a < b:
        print('a小于b')
    else:
        print('a等于b')

function2(4, 5)
function2(10, 10)
