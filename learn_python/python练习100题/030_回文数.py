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
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

def is_palindromic_number(num):
    str_num = str(num)
    if str_num[0] == 0 or len(str_num) != 5:
        print("please input a right number!")
    elif str_num[0] == str_num[-1] and  str_num[1] == str_num[-2]:
        return True
    else:
        return False


print(is_palindromic_number(122311))
