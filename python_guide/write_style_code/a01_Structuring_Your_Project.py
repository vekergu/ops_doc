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
#structuring 机构化
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

#---------------------decorated  装饰器 de co rate d-----------------------------------------
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

#---------------------Dynamic typing----------------------

#Bad
a = 1
a = 'a string'
def a():
    pass  # Do something

#Good
count = 1
msg = 'a string'
def func():
    pass  # Do something

#Bad
items = 'a b c d'  # This is a string...
items = items.split(' ')  # ...becoming a list
items = set(items)  # ...and then a set

#----------------如何  让 字符串 合并 更加的高效--------------------------------
#-------------Mutable and immutable types---------------------
#可变  不可变
my_list = [1, 2, 3]
my_list[0] = 4
print my_list  # [4, 2, 3] <- The same list as changed

x = 6
x = x + 1  # The new x is another object

#Bad
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = ""
for n in range(20):
  nums += str(n)   # slow and inefficient
print nums

#Good
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = []
for n in range(20):
  nums.append(str(n))
print nums
print "good method:","".join(nums)  # much more efficient

#Best
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = [str(n) for n in range(20)]
print nums
print "best method","".join(nums)
# ":".join(string.split())         以:作为分隔符,将所有元素合并为一个新的字符串

#-----------------------------------------------------------
#use join is efficient
foo = 'foo'
bar = 'bar'

foobar = foo + bar  # This is good
foo += 'ooo'  # This is bad, instead you should do:
foo = ''.join([foo, 'ooo'])

foo = 'foo'
bar = 'bar'

foobar = '%s%s' % (foo, bar) # It is OK
foobar = '{0}{1}'.format(foo, bar) # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # It is best
#format    指定输出的格式和内容，format可以输出很多有用信息
