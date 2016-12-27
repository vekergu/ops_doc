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

#--------------------------------------还是反射--------------------------------
#自省
def Activator(request,viewfile,view,action,arg):
    namespace = __import__(viewfile)
    module = getattr(namespace.Views, view)

    func = getattr(module, action)
    result = func(request, arg)

    return result

#------------------------------面向对象-------------------------------
class Province(object):
    #静态字段
    memo = "中国24个省之一"

    #动态方法
    def __init__(self,name,capital,leader,flag=False):
        #动态字段
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        #私有字段
        self.__Thailand = flag

    #静态方法
    @staticmethod
    def Foo():
        print "staticmethod"

    #把方法变为 特性--或者说 属性
    @property
    def Bar(self):
        print self.Name

    def show(self):
        return self.__Thailand
    #私有字段转共有字段
    #只读

    @property
    def Thailand(self):
        return self.__Thailand

    #只写
    @Thailand.setter
    def Thailand(self,value):
        self.__Thailand = value
    #私有方法
    def __sha(self):
        print("my name is world")
    #共有方法
    def sha(self):
        self.__sha()

hb = Province("河北","石家庄","李阳")
sb = Province("山东","济南","王二")

print(hb.Capital)
#对象访问静态字段
print(hb.memo)

print(Province.memo)
#类不能访问动态字段
#print(Province.Name)

Province.memo = "中国24个省之一 cass"
print(hb.memo)

Province.Foo()

#----------------特性 -------------------
hb.Bar

#---------------多态---------------------
#多种对象类型的
#模块 + 反射  可以实现面向对象编程
#封装

#-------------共有 私有--------------------
japan = Province("日本","济南","王二",True)
#japan.__Thailand
japan.show()
print(japan.Thailand)
#japan.__sha()
japan.sha()
#调用私有方法
japan._Province__sha()

#-----------只写特性  只读特性-------------
import time
#访问和修改私有字段
#没有继承object是可读可写
#继承object就能在只读模式下更改字段值
print(japan.Thailand)
japan.Thailand = False
print(japan.Thailand)

# 析构函数 ---------------------------------
#构造函数   用于初始化类的内容部状态，Python提供的构造函数式 __init__();
#析构函数   解释器销毁对象前时想做点啥，就可以写到析构函数内
class Foo:
    #构造函数
    def __init__(self):
        pass
    #析构函数
    def __del__(self):
        print "Foo class 解释器要销毁我了，我要做最后一次的呐喊！！"
    def Go(self):
        print "Go"
    def __call__(self, *args, **kwargs):
        print "call"
f1 = Foo()
f1()  #就会执行__call__方法
#  __call__ 方法

print('-------------------------------类的继承----------------------------')
#基类 父类
class Father(object):
    def __init__(self):
        self.Fname = "ffff"
    def Func(self):
        print "father.func"
    def Bad(self):
        print "father.抽烟喝酒烫头"
#派生类  子类
class Son(Father):
    def __init__(self):
        self.Sname = "ssss"
        #引入父类的构造函数
        #Father.__init__(self)
        super(Son,self).__init__()
    def Bar(self):
        print "son.bar"
    #重写父类方法
    def Bad(self):
        #调用父类的bad方法
        #Father.Bad(self)
        #super(Son,self).Bad()
        print "son.抽烟喝酒"
s1 = Son()
s1.Bar()
s1.Func()
s1.Bad()

print(s1.Fname)

print('----------------------------类的多继承------------------------')
#新式类避免多继承的bug
class A(object):
    def save(self):
        print "A"
class B(A):
    pass
class C(A):
    def save(self):
        print "C"
#经典类 继承是从做到右
class D(B,C):
    pass


temp = D()
temp.save()


#子类可以继承多个类
'''
         class A:
             /\  def save(self):
            /  \
           /    \
          /      \
         /        \
       class B:   class C:
         ^         ^    def save(self):........
          \       /
           \     /
            \   /
             \/
          class D
经典类
新式类  先找b，c 再找A
'''
print('--------------------------新式类--------------------------')
#继承object是新式类  没有就是经典类
'''
定义访问权限
继承多个父类，有同样的方法
    --新式类    深度优先
      经典类    广度优先
'''
print('--------------------------抽象类--------------------------')

from abc import ABCMeta,abstractmethod

class Bar:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Fun(self):pass

class Foo(Bar):
    def __init__(self):
        print '__init__'
    def Fun(self):pass

Foo()
#class Foo如果不使用Fun方法就会报错

print('---------------------------接口--------------------------')
#调用别人的接口
#不写具体实现，只写pass
#泛泛的定义好规则，意义在于架构师写好规范，然后根据规范些内容
#python不是强制类型，可以通过抽象类实现
#抽象类 + 抽象方法 = 接口

print('---------------------------异常处理--------------------------')
