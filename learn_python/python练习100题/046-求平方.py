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
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
'''

TRUE = 1
FALSE = 0
def SQ(x):
    return x * x

again = 1
while again:
    num = int(raw_input('please input number'))
    result = SQ(num)
    if result >= 50:
        again = TRUE
    else:
        again = FALSE