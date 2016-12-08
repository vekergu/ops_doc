#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 顾少
#        Email: vekergu@163.com
#     HomePage: https://github.com/vekergu
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================

def mysum(L):
    if not L:
        return 0
    else:
        return L[0]+mysum(L[1:])

a = mysum([1,2,3,4,5])

def mysum01(L):
    return 0 if not L else L[0] + mysum01(L[1:])


L = [1,2,3,4,5]
sum = 0
for x in L: sum += x




exit(0)