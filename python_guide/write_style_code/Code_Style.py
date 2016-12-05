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
#http://python-guide-zh-cn.readthedocs.io/zh/latest/writing/style.html
#--------------General concepts---------------------
#概念
#Bad
def make_complex(*args):
    x, y = args
    return dict(**locals())

#Good
def make_complex(x, y):
    return {'x': x, 'y': y}


#------One statement per line
#声明
'''
虽然一些复合语句,如允许列表理解和赞赏他们的简洁和表达,
但是很不好的实践，是将两个不相交的语句写在同一行代码。
#Bad
print 'one'; print 'two'

if x == 1: print 'one'

if <complex comparison> and <other complex comparison>:
    pass
    # do something

#Good
print 'one'
print 'two'

if x == 1:
    print 'one'

cond1 = <complex comparison>
cond2 = <other complex comparison>
if cond1 and cond2:
    # do something
'''

#--------------------Function arguments
def complex_function(a, b, c):
    if not a:
        return None  # Raising an exception might be better
    if not b:
        return None  # Raising an exception might be better
    # Some complex code trying to compute x from a, b and c
    # Resist temptation to return x if succeeded
    #if not x:
        pass
        # Some Plan-B computation of x
    #return x  # One single exit point for the returned value x will help
              # when maintaining the code.

#-----------------------Unpacking
Unpacking=[]
for index, item in enumerate(Unpacking):
    pass
    # do something with index and item
# enumerate 可得到每个值的对应位置
for i, n in enumerate(['a','b','c']):
    print i,n

#You can use this to swap variables as well:
a=0
b=1
a, b = b, a
#Nested unpacking works too:

a, (b, c) = 1, (2, 3)
'''
#In Python 3, a new method of extended unpacking was introduced by PEP 3132:
a, *rest = [1, 2, 3]
# a = 1, rest = [2, 3]
a, *middle, c = [1, 2, 3, 4]
# a = 1, middle = [2, 3], c = 4
'''

#-----------------------使用相对位置导入--------------------------------------
from __future__ import absolute_import