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
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
'''


member = [2,3]
denominator = [1,2]
result = 0
def Fibonacci_sequence(N,li):
    for item in range(1,N+1):
        li.append(li[-1] + li[-2])
    return li
member = Fibonacci_sequence(20,member)
denominator = Fibonacci_sequence(20,denominator)

for item in range(20):
    result = result + float(member[item])/denominator[item]

print(result)


#---------------------standarad result----------------------
a = 2.0
b = 1.0
l = []
for n in range(1,21):
    b,a = a,a + b
    l.append(a / b)
print(reduce(lambda x,y: x + y,l))