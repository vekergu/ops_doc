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

#商场收银软件

'''
核心功能是   单价*数量  然后累加



'''

#完成核心工程的程序
def btnOk_button(txtprice,txtnum,lbxlist = None):
    if lbxlist == None:
        lbxlist = []
    totalprice = float(txtprice) * float(txtnum)
    lbxlist.append(totalprice)

#如果商品打8折，打5折呢
#用装饰器？ 不行
#部分商品打折？

#如果增加活动，哪儿核心代码每次都要改动

#如果多个折扣5折，4折，3折，满300送100，满200送50

#采用简单工厂模式
class CashSuper():
    def aceeptCash(money):
        return money

class CashNormal(CashSuper):
    def aceeptCash(money):
        return money

class CashRabet(CashSuper):
    def aceeptCash(money):
        return money

class CashRetrun(CashSuper):
    def aceeptCash(money):
        return money

class CashFactory():
    pass

class btnOk_button():
    pass

#简单工厂的问题是增加了  活动后，要1.新增继承super类的class  2. 改变CashFactory增加选择

#算法时常变动，有什么更好的模式？


#策略模式

class Strategy():
    pass

class ConcreteStrategyA(Strategy):
    pass

class ConcreteStrategyB(Strategy):
    pass

class ConcreteStrategyC(Strategy):
    pass

class Context(object):
    pass

def Main():
    content = Context()


#策略模式 减少算法类 与使用算法类的耦合
#策略模式鸭子举例



class Duck:
    def display(self):
        pass

    def setFlyBehavior(self,fb):
        self.flyBehavior = fb

    def setQuackBehavior(self,qb):
        self.quackBehavior = qb

    def performQuack(self):
        self.quackBehavior.quack()

    def performFly(self):
        self.flyBehavior.fly()


class FlyBehavior:
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Fly with wings.")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Fly no way.")



class QuackBehavior:
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("gua gua")

class Squeak(QuackBehavior):
    def quack(self):
        print("zhi zhi")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("nothing")



class MallardDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Squeak())

    def display(self):
        print("MallardDuck")

class RedheadDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Quack())

    def display(self):
        print("RedheadDuck")

class RubberDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(MuteQuack())

    def display(self):
        print("RubberDuck")

class DecoyDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(MuteQuack())

    def display(self):
        print("DecoyDuck")


for n in MallardDuck(),RedheadDuck(),RubberDuck(),DecoyDuck():
    n.display()
    n.performFly()
    n.performQuack()
    print()

n.setFlyBehavior(FlyNoWay())
n.setQuackBehavior(Quack())
n.display()
n.performFly()
n.performQuack()

#--------------------------------思考-------------------
#有一个大类 鸭子   有颜色熟悉 会叫 会游泳
#绿头鸭 红头鸭  蓝头鸭  继承了这个父类

#那么新增一个熟悉  飞行  就要重写父类和子类， 如果做？
#而且有些鸭子 会飞 有些鸭子  不会飞

#无法用继承来实现

#子类的相同动作的汇聚 可以用策略模式



#简单工厂模式，根据不同的选择，采用不同的类处理

#策略模式，子类中的某些方法共性汇聚