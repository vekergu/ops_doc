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
#http://python.jobbole.com/82534/
#--------------1. 不要使用可变对象作为函数默认值 --------------------

#error
def append_to_list(value, def_list=[]):
    def_list.append(value)
    return def_list

my_list = append_to_list(1)

print(my_list)
my_other_list = append_to_list(2)
print(my_other_list)

import time
def report_arg(my_default=time.time()):
    print(my_default)

report_arg()
time.sleep(1)
report_arg()

#good
def append_to_list(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

my_list = append_to_list(1)

print(my_list)
my_other_list = append_to_list(2)
print(my_other_list)

#------------- 2. 生成器不保留迭代过后的结果-----------
#元组不保留，但是列表没有bug
gen = (i for i in range(5))
print(2 in gen)
print(3 in gen)
print(1 in gen)

a_list = [i for i in range(5)]
print(2 in a_list)
print(3 in a_list)
print(1 in a_list)


#-------------------3. lambda在闭包中会保存局部变量 ----------
#error
my_list = [lambda: i for i in range(5)]
for l in my_list:
    print(l())

#good
my_gen = (lambda: n for n in range(5))

for l in my_gen:
    print(l())

#------------------4. 在循环中修改列表项----------------

x = 10
def fun():
    x +=  1
    print(x)

fun()