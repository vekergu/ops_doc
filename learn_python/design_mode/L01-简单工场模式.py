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
#加减程度，小菜答案
class Program:
    def __init__(self):
        self.A = float(raw_input("请输入数字A:"))
        self.B = raw_input("请输入运算符:")
        self.C = float(raw_input("请输入数字B:"))
    def main_program(self):
        #每个条件都要判断，如果是/,做了3次无用功
        if self.B == "+":
            D = self.A + self.C
        if self.B == "-":
            D = self.A - self.C
        if self.B == "*":
            D = self.A * self.C
        if self.B == "/":  #客户输入0 或者其他字符呢？
            D = self.A / self.C
        return D
#a = Program()
#a.main_program()

#按照代码规范书写
class Program:
    def Main(self):
        strNumberA = float(raw_input("请输入数字A:"))
        strOperate = raw_input("请输入运算符:")
        strNumberB = float(raw_input("请输入数字B:"))
        #每个条件都要判断，如果是/,做了3次无用功
        switcher ={
            "+": strNumberA + strNumberB,
            "-": strNumberA - strNumberB,
            "*": strNumberA * strNumberB,
            "/":    strNumberA / strNumberB if strNumberB else "除数不能为0"
            # "/": (lambda strNumberA,strNumberB : strNumberA / strNumberB if strNumberB else "除数不能为0")(strNumberA,strNumberB)
        }
        result = switcher.get(strOperate)
        return result

#a = Program()
#print(a.Main())

#面向对象
#可维护  可复用  可扩展
#封装 继承  多态

#-----------前进一小步   计算和显示分开
#业务逻辑和计算逻辑分开
#封装
class Operation(object):
    def GetResult(self,strNumberA,strOperate,strNumberB):

        #每个条件都要判断，如果是/,做了3次无用功
        switcher ={
            "+": strNumberA + strNumberB,
            "-": strNumberA - strNumberB,
            "*": strNumberA * strNumberB,
            "/":    strNumberA / strNumberB if strNumberB else "除数不能为0"
            # "/": (lambda strNumberA,strNumberB : strNumberA / strNumberB if strNumberB else "除数不能为0")(strNumberA,strNumberB)
        }
        result = switcher.get(strOperate)
        return result

def Main():
    try:
        strNumberA = float(raw_input("请输入数字A:"))
        strOperate = raw_input("请输入运算符:")
        strNumberB = float(raw_input("请输入数字B:"))
        strResult = Operation()
        print(strResult.GetResult(strNumberA,strOperate,strNumberB))
    except Exception,e:
        print("您的输入有误: %s" %e)

#Main()
'''

#-----------再前进一小步   如何灵活的扩展？
#所谓扩展，就是增加新的功能，但是不去动就的代码
#不去变动运行良好的代码
#继承

#简单工程模式
class Operation(object):
    def __init__(self):
        self.strNumberA = 0
        self.strNumberB = 0
    def NumberA(self):
        pass
    def NumberB(self):
        pass
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def __init__(self):
        super(OperationAdd, self).__init__()
    def GetResult(self):
        result = self.strNumberA + self.strNumberB
        return result

class OperationSub(Operation):
    def __init__(self):
        super(OperationSub,self).__init__()
    def GetResult(self):
        result = self.strNumberA - self.strNumberB
        return result

class OperationMul(Operation):
    def __init__(self):
        super(OperationMul,self).__init__()
    def GetResult(self):
        result = self.strNumberA * self.strNumberB
        return result

class OperationDiv(Operation):
    def __init__(self):
        super(OperationDiv,self).__init__()
    def GetResult(self):
        result =  self.strNumberA / self.strNumberB if self.strNumberB else "除数不能为0"
        return result

class OperationFactory(object):
    def createOperate(self,strOperate):
        switcher ={
            "+": OperationAdd(),
            "-": OperationSub(),
            "*": OperationMul(),
            "/": OperationDiv()
        }
        result = switcher.get(strOperate)
        return result
oper = OperationFactory().createOperate("+")
oper.strNumberA = 1
oper.strNumberB = 2
print(oper.GetResult())