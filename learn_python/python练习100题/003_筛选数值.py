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
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

'''
import math
'''
for i in range(10000):
    #转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print(i)
'''

#-----------standard function----------------

def num_counter(num):
    for i in range(num):
        #转化为整型值
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        if(x * x == i + 100) and (y * y == i + 268):
            yield i

for i in num_counter(10000000):
    print(i)