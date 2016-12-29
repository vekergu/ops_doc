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
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
'''

M=0
for i in range(1,21):
    N=1
    for j in range(1,i+1):
        N = j*N
    M = M+N

print(M)

#----------------standarad result-------------------------------
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,l))
print('1! + 2! + 3! + ... + 20! = %d' % s)

#-------------optimize progrocess------------------

