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

#list
testList = [10086,'中国移动',[1,2,4,5]]

print(len(testList))
print(testList[1:])
testList.append('i\'m new here!')

print(len(testList))
print(testList[-1])

print(testList.pop(1))
print(len(testList))
print(testList)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix]
print(col2)

col2even = [row[1] for row in matrix if row[1] % 2 == 0]
print(col2even)