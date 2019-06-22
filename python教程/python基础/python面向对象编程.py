# -*- coding: utf-8 -*-

'''概述
面向对象编程也叫OOP编程, 面向对象编程更适合大型项目开发
'''

'''类和对象
类: 具有某种特征事物的集合
对象: 集合中的个体
类是抽象的, 对象是具体的
'''

# 类
class ClassName:
    pass


# 类被实例化后叫对象
cn = ClassName()


# 构造函数(构造方法)
'''
self代表类本身
构造函数的实际意义就是初始化
'''
class ClassName2:
    def __init__(self):
        print('I am ClassName2 self')

cn2 = ClassName2()


# 给类加参数:就是给构造方法加参数
class ClassName3:
    def __init__(self, name, job):
        print('My name is {} My job is {}'.format(name, job))

cn3 = ClassName3('tom', 'teacher')


'''属性和方法
属性: 静态特征, 类里面的变量
方法: 动态特征, 类里面的函数
'''
class ClassName4:
    def __init__(self, name, job):
        self.myname = name
        self.myjob = job

    def function(self, name):
        print('hello %s!' %name)
        print('hello %s!' %self.myname)
# 实例化,并调用类的属性
cn4 = ClassName4('tom', 'teacher')
cn4.myname
cn4.myjob
cn4.function('cat')


'''继承和重载
继承: 把某一个或多个类(基类)的特征拿过来
重载: 在子类(派生类)里面对继承的特征重新定义
父类: 基类
子类: 派生类
'''

# 继承(单继承, 多继承)
class FatherClass():
    def __init__(self):
        self.word = 'can say'

    def say(self):
        print(self.word)

class MotherClass():
    def write(self):
        print('I can write')

class SonClass(FatherClass):
    pass

class Daughter(FatherClass, MotherClass):
    def listen(self):
        print('I can listen')

class SonClass2(FatherClass):
    def say(self):
        print('I Can say more word')

sc = SonClass()
sc.say()

d = Daughter()
d.say()
d.write()
d.listen()

sc2 = SonClass2()
sc2.say()
