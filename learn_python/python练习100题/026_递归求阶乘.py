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
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!

'''

def factorial(num):
    fn = 0
    if num == 0:
        fn = 1
    else:
        fn = factorial(num-1)*num
    return fn


print(factorial(4))

