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
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
'''
import copy
li = [1,2,3]

a = copy.deepcopy(li)
print(a)

a = []
for item in li:
    a.append(item)

print(a)

a = []

a = li[:]
print(a)
li[1] = 4
a[2] = 6
print(a)
print(li)