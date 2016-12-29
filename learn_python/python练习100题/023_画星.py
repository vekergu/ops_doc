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
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''

from sys import stdout

for i in range(4):
    for j in range(2-i+1):
        stdout.write(" ")
    for k in  range(2 * i + 1):
        stdout.write("*")
    print()
for i in range(3):
    for j in range(i+1):
        stdout.write(" ")
    for k in  range(4 - 2 * i + 1):
        stdout.write("*")
    print()