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
题目：两个变量值互换。
'''

def exchange(a,b):
    a,b = b,a
    return (a,b)

if __name__ == "__main__":
    x = 10
    y = 20
    print("x = %d,y = %d" %(x,y))
    x,y = exchange(x,y)

    print('x = %d,y = %d' %(x,y))