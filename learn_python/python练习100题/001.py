#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 白开水
#        Email: vekergu@163.com
#     HomePage: https://github.com/vekergu
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================
from __future__ import print_function
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
'''
li = []

for h in range(1,5):
    for j in range(1,5):
            for k in range(1,5):
                x = (h,j,k)
                if len(list(set(x))) == 3:
                    li.append(x)

print(len(li))
print(li)
'''

#-----------------------标准答案------------------------------

#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print(i,j,k)


#递归出[1,2,3,4]所有的三位数字

digit = 3

import itertools
#去重  有序
print(list(itertools.permutations([1,2,3,4],2)))
#去重 无序
print(list(itertools.combinations([1,2,3,4],2)))

print(list(itertools.permutations([1,2,3,4],3)))
print(list(itertools.combinations([1,2,3,4],3)))




#给定一个列表中的组合，计算此列表可以组合多少位互不相同无重复的数字

