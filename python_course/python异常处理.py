# -*- coding: utf-8 -*-

# 为防止程序因为出现异常而终止, 必须对可能出现的异常进行处理

# 异常处理示例
for i in range(10):
    print(i)
    if i == 4:
        try:
            print(number)
        except Exception as err:
            continue
