# -*- coding: utf-8 -*-

# 自定义异常
class CustomError(Exception):
    def __init__(self, sexerror):
        self.sexerror = sexerror

    def __str__(self):
        return self.sexerror

# 异常抛出
boy = ['男', '男', '男', '女']
for i in boy:
    if i == '女':
        raise CustomError('性别错误, 不允许出现女性')
