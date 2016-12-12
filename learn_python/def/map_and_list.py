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
from functools import reduce
#-----------------------filter 和 reduce---------------------
print(range(-5,5))
print(filter((lambda x:x>0),range(-5,5)))
print(reduce((lambda x,y:x+y),range(1,5)))
print(reduce((lambda x,y:x*y),range(1,5)))

#----------------------列表解析与map-------------------------
#map调用比等效for循环快2倍
#列表解析往往比map调用稍快一些
print(ord('s'))

res = []
for x in 'spam':
    res.append(ord(x))

print(res)

#map调用
res = list(map(ord,'spam'))
print(res)

#列表解析
res = [ord(x) for x in 'spam']
print(res)

print([x**2 for x in range(10)])
print(list(map(lambda x:x**2,range(10))))

#---------------------------增加测试和嵌套循环----------------------
print([x for x in range(5) if x % 2 == 0 ])
print(list(filter((lambda x:x % 2 == 0),range(5))))

print(map( (lambda x:x**2),  filter((lambda x:x%2 ==0),range(10))  ))

res = [x+y for x in [0,1,2] for y in [100,200,300,]]
print(res)

print([x + y for x in 'spam' for y in 'SPAM'])

print([(x,y) for x in range(5) if x % 2 == 0  for y in range(5) if y % 2 == 1])

#------------------------列表解析 和 矩阵 ------------------------------

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
N = [[2,2,2],
     [3,3,3],
     [4,4,4]]

print([row[1] for row in M])

print([M[row][1] for row in (0,1,2)])

print([M[i][i] for i in range(len(M))])

print([M[row][col]*N[row][col] for row in range(3) for col in range(2)])

print([[M[row][col]*N[row][col] for col in range(3)] for row in range(3)])

#----------------------列表解析--------------------------------------------
#map调用比等效for循环快2倍
#列表解析往往比map调用稍快一些