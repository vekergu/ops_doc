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
题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。
'''

li = ["a",12,[23],"34"]
l = []
for item in reversed(li):
    l.append(item)

for i in li[::-1]:
	print(i)

print(l)