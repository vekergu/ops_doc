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
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
程序分析：无。
'''

def play_game(n,m):
    li = range(1,n+1)
    index = 1
    while len(li) != 1:
        for item in range(len(li)):
            if index != m:
                index += 1
                len_li = len(li)
            else:
                index = 1
                li[item] = 0
            if  len(li)  - item  == 1:
                li = filter(lambda x:x !=0,li)
    return li[0]


print(play_game(4,4))