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
题目：八进制转换为十进制
'''

if __name__ == "__main__":
    n = 0
    p = raw_input("input a octal number:\n")
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord("0")

    print(n)

