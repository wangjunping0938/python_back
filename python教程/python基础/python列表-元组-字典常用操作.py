# -*- coding: utf-8 -*-

list1 = ['Python', 'PHP', 'Go', 'Shell', 'Java', 'C++', 'C#']
tuple1 = ('Python', 'PHP', 'Go', 'Shell', 'Java', 'C++', 'C#')
dict1 = {'Python':'机器学习', 'PHP':'web开发', 'Go':'机器学习&web开发',
         'Shell':'运维脚本', 'Java':'全站'}

# 列表和元组遍历方式一致
for i in list1:
    print(i)

for i in range(len(list1)):
    print('第%s次: %s' %(i, list1[i]))

# 字典便利
for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for k, v in dict1.items():
    print('Key:%s, Value:%s' %(k, v))
