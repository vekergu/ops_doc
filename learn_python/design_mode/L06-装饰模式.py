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

#装饰过的对象可替代原始对象

'''
原则：
类应该对扩展开放，对修改关闭。
案例：
奶茶店有多种饮料：奶茶、果汁、咖啡；每种饮料可搭配若干配料：珍珠、布丁、牛奶；要能根据顾客的任意搭配下单并计算价钱；
'''



class Beverage:
    description = "Unknown Beverage"

    def get_description(self):
        return self.description

    def cost(self):
        pass


class CondimentDecorator(Beverage):
    def get_description(self):
        pass


class MilkyTea(Beverage):
    def __init__(self):
        self.description = "MilkyTea"

    def cost(self):
        return 1.99


class FruitJuice(Beverage):
    def __init__(self):
        self.description = "FruitJuice"

    def cost(self):
        return 1.80


class Coffee(Beverage):
    def __init__(self):
        self.description = "Coffee"

    def cost(self):
        return 2.00


class Pearl(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " + Pearl"

    def cost(self):
        return 1.50 + self.beverage.cost()


class Pudding(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " + Pudding"

    def cost(self):
        return 1.60 + self.beverage.cost()


class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " + Milk"

    def cost(self):
        return 2.10 + self.beverage.cost()


if __name__ == '__main__':
    b = FruitJuice()
    print("%s = $%s\n" % (b.get_description(), b.cost()))

    b = MilkyTea()
    b = Pearl(b)
    b = Pudding(b)
    print("%s = $%s\n" % (b.get_description(), b.cost()))

    b = Coffee()
    b = Pearl(b)
    b = Milk(b)
    print("%s = $%s\n" % (b.get_description(), b.cost()))