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

#-------------------------------Check if variable equals a constant------------
attr = True
#bad
if attr == True:
    print 'True!'

if attr == None:
    print 'attr is None!'
#Good:
# Just check the value
if attr:
    print 'attr is truthy!'

# or check for the opposite
if not attr:
    print 'attr is falsey!'

# or, since None is considered false, explicitly check for it
if attr is None:
    print 'attr is None!'

#-------------------------------Access a Dictionary Element----------------------
#Bad:

d = {'hello': 'world'}
if d.has_key('hello'):
    print d['hello']    # prints 'world'
else:
    print 'default_value'
#Good:

d = {'hello': 'world'}

print d.get('hello', 'default_value') # prints 'world'
print d.get('thingy', 'default_value') # prints 'default_value'

# Or:
if 'hello' in d:
    print d['hello']

#----------------------------------------Short Ways to Manipulate Lists------------------
#Bad:

# Filter elements greater than 4
a = [3, 4, 5]
b = []
for i in a:
    if i > 4:
        b.append(i)
#Good:

a = [3, 4, 5]
b = [i for i in a if i > 4]
# Or:
b = filter(lambda x: x > 4, a)
#Bad:

# Add three to all list members.
a = [3, 4, 5]
for i in range(len(a)):
    a[i] += 3
#Good:

a = [3, 4, 5]
a = [i + 3 for i in a]
# Or:
a = map(lambda i: i + 3, a)
#Use enumerate() keep a count of your place in the list.

a = [3, 4, 5]
for i, item in enumerate(a):
    print i, item
# prints
# 0 3
# 1 4
# 2 5

#-------------------------------Read From a File----------------------
#Bad:
f = open('file.txt')
a = f.read()
print a
f.close()

#Good:
with open('file.txt') as f:
    for line in f:
        print line


#--------------------------------Line Continuations--------------------------
#Bad:

my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”"""
'''
from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
    yet_another_nice_function
    '''
#Good:

my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)
'''
from some.deep.module.inside.a.module import (
    a_nice_function, another_nice_function, yet_another_nice_function)
    '''

