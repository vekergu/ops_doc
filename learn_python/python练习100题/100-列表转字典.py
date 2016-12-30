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
列表转换为字典。
'''

li = ["a","b","c"]
di = {}

for index,value in enumerate(li):
    di[index] = value

print(di)

i = ['a', 'b']
l = [1, 2]
print(dict([i]))
print(dict([i,l]))