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
#----------------------生成器------------------------------------------------
def gensquares(N):
    for i in range(N):
        yield i**2

for i in gensquares(5):
    print(i,end=' : ')

x = gensquares(4)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#------------扩展生成器协议 send 和 next ----------------------
