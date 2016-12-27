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
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''


f0 = 0
f1 = 1
fn_1 = 1
fn_2 = 0
for i in range(2,10):
    fn = fn_1 + fn_2
    print(fn)
    fn_2 = fn_1
    fn_1   = fn

f = []
f.append(0)
f.append(1)
for i in range(2,11):
    f.append(f[-1] + f[-2])
print(f)


# 使用递归
def fib(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

# 输出了第10个斐波那契数列
print(fib(3))


#---------use recursion stdout list ------------------
def fib_list(n,result_list=[]):
    if n == 0:
        result_list.append(0)
        return result_list
    elif n==1:
        result_list.append(0)
        result_list.append(1)
        return result_list
    result_list.append(fib_list(n-1)[-2] + fib_list(n-2)[-1] )
    return result_list

# 输出了第10个斐波那契数列
print(fib_list(2))
#error
