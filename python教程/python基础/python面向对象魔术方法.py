# -*- coding: utf-8 -*-

# 在特定情况下自动触发的方法, 例如构造方法
class Man():
    foot = '脚'
    hand = '手'
    body = '身体'
    head = '头'

    # 自动初始化数据方法
    def __init__(self, name, sex, height):
        print('自动初始化数据方法')
        self.name = name
        self.sex = sex
        self.height = height

    def __del__(self):
        print('自动执行,析构函数')

    def eat(self):
        print('%s 可以吃饭了' %self.name)

    def say(self):
        print('身高:{} 性别:{} 名字:{}'.format(self.height, self.sex, self.name))


if __name__ == '__main__':
    m = Man('tom', '男', '175cm')
    m.say()
