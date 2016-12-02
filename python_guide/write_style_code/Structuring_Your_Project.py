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
#http://python-guide-zh-cn.readthedocs.io/zh/latest/writing/structure.html#structure-is-key
#--------------------how to import a model -------------------------------------------------------
'''
#Very bad
[...]
from pip import *
[...]
x = sqrt(4)  # Is sqrt part of modu? A builtin? Defined above?

#Better
from pip import sqrt
[...]
x = sqrt(4)  # sqrt may be part of modu, if not redefined in between

#Best
import pip
[...]
x = pip.sqrt(4)  # sqrt is visibly part of modu's namespace
'''

#---------------------decorated  装饰器-----------------------------------------
def foo():
    pass
    # do something

def decorator(func):
    # manipulate func
    return func

foo = decorator(foo)  # Manually decorate
#把这个函数对象作为一个参数，在另一个函数执行后
#在进行执行
foo()

@decorator
def bar():
    pass
    # Do something
# bar() is decorated

