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
题目：按相反的顺序输出列表的值。
'''
li = ["a",12,[23],"34"]
l = []
for item in reversed(li):
    l.append(item)

for i in li[::-1]:
	print(i)

print(l)