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
'''
定义：不要存在多于一个导致类变更的原因。通俗的说，即一个类只负责一项职责。
问题由来：
    类T负责两个不同的职责：职责P1，职责P2。
    当由于职责P1需求发生改变而需要修改类T时，有可能会导致原本运行正常的职责P2功能发生故障。
解决方案：
    遵循单一职责原则。分别建立两个类T1、T2，
    使T1完成职责P1功能，T2完成职责P2功能。
    这样，当修改类T1时，不会使职责P2发生故障风险；
    同理，当修改T2时，也不会使职责P1发生故障风险。

所谓职责扩散，就是因为某种原因，职责P被分化为粒度更细的职责P1和P2。
    类T只负责一个职责P，这样设计是符合单一职责原则的。
    后来由于某种原因，也许是需求变更了，也许是程序的设计者境界提高了，需要将职责P细分为粒度更细的职责P1，P2，
    这时如果要使程序遵循单一职责原则，需要将类T也分解为两个类T1和T2，分别负责P1、P2两个职责。
    但是在程序已经写好的情况下，这样做简直太费时间了。
    所以，简单的修改类T，用它来负责两个职责是一个比较不错的选择，虽然这样做有悖于单一职责原则。
'''
#----------------演变开始------------
class Animal:
    def breathe(self,animal):
        print(animal,"呼吸空气")


class Client:
    def main(self):
        animal = Animal()
        animal.breathe("牛")
        animal.breathe("羊")
        animal.breathe("猪")


Client().main()

print("--------增加需求   鱼是不呼吸的------------")
class Terrestrial:
    def breathe(self,animal):
        print(animal,"呼吸空气")
class Aquatic:
    def breathe(self,animal):
        print(animal,"呼吸水")

class Client:
    def main(self):
        terrestrial = Terrestrial()
        terrestrial.breathe("牛")
        terrestrial.breathe("羊")
        terrestrial.breathe("猪")

        aquatic = Aquatic()
        aquatic.breathe("鱼")

Client().main()

print("------------偷懒的做法---------------------")
class Animal:
    def breathe(self,animal):
        if animal != "鱼":
            print(animal,"呼吸空气")
        else:
            print(animal, "呼吸水")



class Client:
    def main(self):
        animal = Animal()
        animal.breathe("牛")
        animal.breathe("羊")
        animal.breathe("猪")
        animal.breathe("鱼")

Client().main()

print("-------------不改变原代码，不用单一职责原则-----------")
class Animal:
    def breathe(self,animal):
        print(animal,"呼吸空气")

    def breathe1(self, animal):
        print(animal, "呼吸水")



class Client:
    def main(self):
        animal = Animal()
        animal.breathe("牛")
        animal.breathe("羊")
        animal.breathe("猪")
        animal.breathe1("鱼")

Client().main()
