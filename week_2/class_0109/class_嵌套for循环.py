# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 21:17
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_嵌套for循环.py

#嵌套for循环
# d={'name':{'boboji':'钵钵鸡','snow':'小雪','luren':'路人'},
#    'score':[99,100,120]}
# # print(d['name'])
# # print(d['score'])
# #字典里面嵌套了列表和字典
# #for循环遍历字典的时候  遍历的是key
# for key in d:
#     print(d[key])
#     for item in d[key]:
#         print(item)
#

list1 = [[2, 3, 8, 4, 9, 5, 6],[5, 6, 10, 17, 11, 2]]
#请你利用刚刚所学的for循环 然后我们把每一个元素都读取出来
for item in list1:
    print(item)#1

    for y in item:#2
        print(y,end=' ')

    print()#3

