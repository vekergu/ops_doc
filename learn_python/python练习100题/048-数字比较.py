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
题目：数字比较。
'''

if __name__ == '__main__':
    i = 10
    j = 20
    if i > j:
        print('%d 大于 %d' %(i,j))
    elif i == j:
        print('%d 等于 %d' %(i,j))
    elif i < j:
        print('%d 小于 %d' %(i,j))
    else:
        print("未知")