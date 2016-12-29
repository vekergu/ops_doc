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
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
'''

letter = raw_input("please input:")
#while letter  != 'Y':
if letter == 'S':
    print ('please input second letter:')
    letter = raw_input("please input:")
    if letter == 'a':
        print ('Saturday')
    elif letter  == 'u':
        print ('Sunday')
    else:
        print ('data error')

elif letter == 'F':
    print ('Friday')

elif letter == 'M':
    print ('Monday')

elif letter == 'T':
    print ('please input second letter')
    letter = raw_input("please input:")

    if letter  == 'u':
        print ('Tuesday')
    elif letter  == 'h':
        print ('Thursday')
    else:
        print ('data error')

elif letter == 'W':
    print ('Wednesday')
else:
    print ('data error')