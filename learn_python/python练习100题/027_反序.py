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
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析：无。
'''

input = "abcde"
str=""
for item in reversed(input):
    str = "".join([str,item])

print(str)


#-------------use recursion --------------------

def revers_str(str,li = len(str)):
    if li == 0:
        return
    print(str[li-1])
    revers_str(str,li-1)

revers_str(str)



