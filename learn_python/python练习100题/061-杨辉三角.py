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
题目：打印出杨辉三角形（要求打印出10行如下图）。
程序分析：无。
'''

a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
for j in range(10):
    a[i][0] = 1
    a[i][i] = 1
for i in range(2,10):
    for j in range(1,i):
        a[i][j] = a[i - 1 ][j - 1] + a[ i - 1][j]
print(a)
from sys import stdout
for i in range(10):
    for j in range(i + 1):
        stdout.write(str(a[i][j]))
        stdout.write(" ")
    print()
