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

if __name__ == "__main__":
    str1 = raw_input("input string:\n")
    str2 = raw_input("input string:\n")
    str3 = raw_input("input string:\n")
    print(str1,str2,str3)

    if str1 > str2 : str1,str2 = str2,str1
    if str1 > str3 : str1,str3 = str3,str1
    if str2 > str3 : str2,str3 = str3,str2

    print("after being sorted.")
    print(str1,str2,str3)