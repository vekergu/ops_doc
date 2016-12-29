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
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''

li = [1,23,4,55]

min_li = min(li)
index_li = li.index(min_li)

end_li = li[-1]
li[-1] = min_li
li[index_li] = end_li
print(li)