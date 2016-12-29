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
题目：使用lambda来创建匿名函数。
'''

MAXIMUM = lambda x,y : (x > y) * x + (x < y) * y
MINIMUM = lambda x,y : (x > y) * x + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('the largar one is %d' %MAXIMUM(a,b))
    print('the lower one is %d' %MINIMUM(a,b))



