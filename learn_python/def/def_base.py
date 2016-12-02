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

#--------------------------------------函数与属性---------------------------------------------------
#可以为函数添加属性，那么是否直接影响所有的函数？
def func():
    pass

func()
func.attr = "value"

#----------------------------------------函数多态--------------------------------------------------
#定义和调用
def times(x,y):
    return x*y

print times(2,4)

x=times(3.14,4)
print x

print  times("Ni",4)

#函数内的运算针对处理的对象进行了随机应变，这种依赖类型的行为称为多态

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = "SPAM"
s2 = "SCPM"

print intersect(s1,s2)

print [x for x in s1 if x in s2]

#多态
x = intersect([1,2,3],(1,4))
print x

#------------------------------------------------------函数作用域-----------------------------------------
#变量名解析LEGB原则
#首先是本地
#然后是函数内
#然后是全局
#最后是内置

X = 99
def fun(Y):
    z = X + Y
    return z

print fun(1)

#内置作用域
#就是__builtin__的内置模块
import __builtin__
print [x if "open" in dir(__builtin__) else "none"]
#这个变量中的列表组成了python的内置作用域
print __builtin__.open

def hider():
    open = "SVG"
    #open('data,txt')
#这样写法是错的，open就不是一个内置函数了

x1 = 99
def fun1():
    x1 = 88
    return x1

print "fun1",fun1()
print  "x1",x1

#-------------global 使用------------
x2 = 99
def fun2():
    global x2
    x2 = 88
    return x2

print "func:",fun2()
print  "x2:",x2


y3,z3 = 1,2
def all_global():
    global x3
    x3 = y3 + z3
    return x3
print "all_global:", all_global()


#----------最小化全局变量------------------

x4 = 99
def fun4():
    global x4
    x4 = 99
    return x4

def fun5():
    global x4
    x4 = 77
    return x4

print "fun4",fun4()
print "x4",x4
print "fun5",fun5()
print "x4",x4

#-------------最小化文件间修改-----------------------
'''
#first.py
x=99
def setx(new):
    global x
    x = new
    return x
#second.py
import first
print(first.x)
first.x = 88
'''

#----------------作用域和嵌套函数------------------------
x6 =99
def fun6():
    x6 =88
    def fun7():
        print(x6)
    fun7()
fun6()


#------------------工厂函数------------------------------

def maker(N):
    def action(x):
        return N ** x
    return action

f = maker(2)
print f(2)
print f(3)
#第一次定义f参数2是给N赋值
#后面的f(2)是给x赋值

#---------------------------------------nonloacl语句--------------------------------------------

def tester(start):
    state = start
    def nested(label):
        print(label,state)
        #state +=1      默认情况下，不容许修改嵌套的def作用域中的名称
    return nested
'''
#nonloacl 是python3.0引入的
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label,state)
        state +=1
    return nested

F = test(0)
f('ham')
'''