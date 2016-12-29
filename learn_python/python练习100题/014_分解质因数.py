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
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''

from math import sqrt
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_prime_factor(num,item,li = []):
    if item == num :
       li.append(item)
       return li
    elif num%item == 0:
       li.append(item)
       is_prime_factor(int(num/item),item)
    else:
        is_prime_factor(num,item+1)
    return li

def get_prime_factor(num):
    for item in range(0,num):
        if num == 1:
            li = [1]
            return li
        elif is_prime(item):
            li = is_prime_factor(num,item)
            return li


print(get_prime_factor(1))

#-----------------------optimize-----------------------

def prime_factor(n):
    if not isinstance(n, int) or n <= 0 :
        print('请输入一个正确的数字 !')
        exit(0)
    elif n in [1] :
        print('{}'.format(n))
    while n not in [1] : # 循环保证递归
        for index in xrange(2, n + 1) :
            if n % index == 0:
                n /= index # n 等于 n/index
                if n == 1:
                    print(index)
                else : # index 一定是素数
                    print('{} *'.format(index),)
                break