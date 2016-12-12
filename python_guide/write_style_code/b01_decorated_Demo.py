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
#代码参考自： http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
#demo 1  ------作为引子
print  "---------demo 01---------------------"
def myfunc():
    print "myfunc() called."

myfunc()
myfunc()

#demo2    -------使用装饰函数在函数执行前和执行后分别附加额外功能
print  "---------demo 02---------------------"
def deco(func):
    print "before myfunc() called."
    func()
    print "  after myfunc() called."
    return func

def myfunc():
    print " myfunc() called."

myfunc = deco(myfunc)
myfunc()

myfunc()
#只有调用第一函数会执行额外功能
#是因为有myfunc = deco(myfunc)对myfunc进行功能添加
#为什么没有继承给第二个调用？deco(myfunc)()  --->func()  ---> print
#--------理解错误更正------------------------------
#1. myfunc已经是在执行了deco(myfunc)
#所以最后还有2个print(" myfunc() called.")

#demo3  ----使用语法糖@来装饰函数
print  "---------demo 03---------------------"
def deco(func):
    print "before myfunc() called."
    func()
    print "  after myfunc() called."
    return func

@deco     #--->  myfunc = deco(myfunc)
def myfunc():
    print " myfunc() called."

myfunc()
myfunc()
#在语句执行到@deco已经执行了函数
#所以下面的myfunc()只是单纯的执行的myfunc函数

#demo04  -----标准装饰器用法
#如果根据demo02如何使每次调用myfunc()都会执行demo(myfunc)？
#让demo(myfunc)只返回一个函数名，而不执行变更的内容，而且重新定义了函数
print  "---------demo 03---------------------"
def deco(func):
    def  _demo():
        print "before myfunc() called."
        func()
        print "  after myfunc() called."
    return  _demo

@deco     #--->  myfunc = deco(myfunc)  --> _demo(myfunc)
          #因为没有调用_demo的动作，只是将_demo返回，也就是重新定义了myfunc这个函数
def myfunc():
    print(" myfunc() called.")

myfunc()
myfunc()
#这个方法是根据要求推出了的，居然与答案一致，哈哈
#感谢张云贵童鞋从简到难的引导

#demo4  ----对带参数的函数进行装饰
print  "---------demo 04---------------------"
def deco(func):
    def  _demo(x,y):
        print"before myfunc() called."
        func(x,y)
        print"  after myfunc() called."
    return  _demo

@deco     #--->  myfunc = deco(myfunc)  --> _demo(myfunc)
          #因为没有调用_demo的动作，只是将_demo返回，也就是重新定义了myfunc这个函数
def myfunc(a,b):
    print " myfunc() called.",a,b

myfunc('x','y')
myfunc('m','n')

#demo5  ----对数量不确定参数的函数进行装饰
print  "---------demo 05---------------------"
def deco(func):
    def  _demo(*args,**kwargs):
        print"before myfunc() called."
        func(*args,**kwargs)     #这里要注意
        print"  after myfunc() called."
    return  _demo

@deco     #--->  myfunc = deco(myfunc)  --> _demo(myfunc)
          #因为没有调用_demo的动作，只是将_demo返回，也就是重新定义了myfunc这个函数
def myfunc(*args,**kwargs):
    print " myfunc() called.",args,kwargs

myfunc('x','y','z','f')
myfunc('m','n',0,1,2,3)
#*args 是已元组的方式出现
#**kwargs是以字典的方式出现。

#demo6  ----让装饰器带参数
#尝试了不定参，失败，从最简单开始
print  "---------demo 06---------------------"
def deco(arg):
    def  _demo(func):
        def __demo():
            print"before myfunc() called.",arg
            func()     #这里要注意
            print"  after myfunc() called.",arg
        return  __demo    #注意return的位置，不要写错
    return _demo

#myfunc = deco(myfunc)("decorated args")          #需要确定是deco(myfunc) -->  _demo("decorated args")



#@deco("decorated args")     #--->  myfunc = deco(myfunc)("decorated args")
                              #deco ——> _demo  --> __demo
                              #deco(myfunc)("decorated args") --> _demo("decorated args") --> __demo
          #因为没有调用_demo的动作，只是将_demo返回，也就是重新定义了myfunc这个函数
def myfunc():
    print " myfunc() called."
                                                  #还是deco(myfunc)("decorated args") ......???
#myfunc = deco("decorated args")(myfunc)
#myfunc =   _deco(myfunc)

myfunc()
myfunc()
#*args 是已元组的方式出现
#**kwargs是以字典的方式出现。


#demo7  ----让装饰器带参数，可变参
print  "---------demo 07---------------------"
def deco(*args,**kwargs):
    def  _demo(func):
        def __demo(*margs,**mkwargs):
            print"before myfunc() called.",args,kwargs
            func(*margs,**mkwargs)     #这里要注意
            print"  after myfunc() called.",args,kwargs
        return  __demo
    return _demo


@deco("decorated args")     #--->  myfunc = deco(myfunc)("decorated args")
                              #deco ——> _demo  --> __demo
                              #deco(myfunc)("decorated args") --> _demo("decorated args") --> __demo
          #因为没有调用_demo的动作，只是将_demo返回，也就是重新定义了myfunc这个函数
def myfunc(*args,**kwargs):
    print " myfunc() called.",args,kwargs

myfunc('x','y','z','f')
myfunc('m','n',0,1,2,3)
#*args 是已元组的方式出现
#**kwargs是以字典的方式出现。


#demo8  ----让装饰器带让装饰器带 类 参数
print  "---------demo 08---------------------"
class locker:
    def __init__(self):
        print("I am a class")
    def active(self):
        print "locker.acquire() called.（这是动态方法）"
    @staticmethod
    def acquire():
        print "locker.acquire() called.（这是静态方法）"

    @staticmethod
    def release():
        print "  locker.release() called.（不需要对象实例）"
def deco(cls):
    def  _demo(func):
        def __demo(*margs,**mkwargs):
            #a = cls()
            #a.active()
            cls.acquire()
            print"before myfunc() called."
            func(*margs,**mkwargs)     #这里要注意
            print"  after myfunc() called."
            cls.acquire()
        return  __demo
    return _demo
#使用动态方法不创建实例会报错

@deco(locker)     #--->  myfunc = deco(myfunc)("decorated args")
                              #deco ——> _demo  --> __demo
                              #deco(myfunc)("decorated args") --> _demo("decorated args") --> __demo
          #因为没有调用_demo的动作，只是将_demo返回，也就是重新定义了myfunc这个函数
def myfunc(*args,**kwargs):
    print " myfunc() called.",args,kwargs

myfunc('x','y','z','f')
myfunc('m','n',0,1,2,3)
#*args 是已元组的方式出现
#**kwargs是以字典的方式出现。

'''
#demo9  ----装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装
#没有验证，直接应用原文了
# -*- coding:gbk -*-
#mylocker.py: 公共类 for 示例9.py

class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("  mylocker.unlock() called.")

class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")

def lockhelper(cls):
   #cls 必须实现acquire和release静态方法
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco

# -*- coding:gbk -*-
#示例9: 装饰器带类参数，并分拆公共类到其他py文件中同时演示了对一个函数应用多个装饰器

#from mylocker import *

class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print(" myfunc() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b

if __name__=="__main__":
    a = example()
    a.myfunc()
    print(a.myfunc())
    print(a.myfunc2(1, 2))
    print(a.myfunc2(3, 4))
    '''