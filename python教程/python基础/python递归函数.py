# -*- coding: utf-8 -*-

# 调用函数自己本身的函数
def getall(number, total):
    total = total * number * number / 2
    if (number / 4 >= 10):
        if (number/8 >= 10):
            getall(number/4, total)
        else:
            print(total * number / 4)
    else:
        print(total)

getall(10, 1)
