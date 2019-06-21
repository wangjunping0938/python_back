# -*- coding: utf-8 -*-

# 三种控制流
# 1. 顺序结构
# 2. 条件分支结构
# 3. 循环结构


# 条件分支结构
# if语句
a = 10
b = 1
if (a > 9):
    print('a>9')
    if b == 9:
        print('b<9')
elif a > 9 and b < 19:
    print('19>a>9')
else:
    print('以上条件都不满足')

# while循环语句
a = 0
while a < 10:
    print('while循环')
    a += 1

# for循环语句
lst = ['aa', 'bb', 'cc', 'dd']
for i in lst:
    print(i)
for i in range(10):
    print('for循环')

# 中断结构, break, continue
# break中断全部循环, continue中断一次
for i in range(10):
    if i == 5:
        break
    print('break中断全部循环')

for i in range(10):
    if i == 5:
        continue
    print('continue中断一次')


# 输出乘法口诀
for i in range(10):
    for j in range(1, i+1):
        print('%s*%s=%s' %(j, i, i*j), end=" ")
    print()

print()
print()
# 逆向输出乘法口诀
for i in reversed(range(1, 10)):
    for j in reversed(range(1, i+1)):
        print('{}*{}={}'.format(i, j, i*j), end=' ')
    print()
