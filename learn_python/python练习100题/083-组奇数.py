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
题目：求0—7所能组成的奇数个数。
'''
import itertools

#去重  有序
print(list(itertools.permutations([1,2,3,4],2)))
#去重 无序
print(list(itertools.combinations([1,2,3,4],2)))

sum = 4
s = 4
for  j in range(2,9):
    print(sum)
    if j <= 2:
        s *= 7
    else:
        s *= 8
    sum += s
print("sum = %d" %sum)

print(len(list(itertools.permutations(range(0,8),7))))

