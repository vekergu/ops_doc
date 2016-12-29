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
题目：模仿静态变量(static)另一案例。
程序分析：演示一个python作用域使用方法
'''

class Num:
    nNum = 1
    def inc(self):
        self.nNum +=1
        print('nNum = %d' %self.nNum)

nNum = 2
inst = Num()
for i in range(3):
    nNum +=1
    print("The num = %d" %nNum)
    inst.inc()