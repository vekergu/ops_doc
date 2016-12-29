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
题目：学习使用auto定义变量的用法。
程序分析：没有auto关键字，使用变量作用域来举例吧。
'''

num = 2
def autofunc():
    num = 1
    print('internal block num = %d' %num)
    num += 1
for i in range(3):
    print("the num = %d" %num)
    num +=1
    autofunc()