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
题目：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''

for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print('%d * %d = % -3d' % (i,j,result))
    print('')