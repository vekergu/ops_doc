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

#http://www.cnblogs.com/itlinux/p/5716192.html
from __future__ import print_function
#input默认输入的是字符串，要转化成数字类型需要强转。
#在python2.#中raw_input和python3.#的input的作用完全相同。
#在python2.#中input输入的是什么类型就是什么类型。
print("------------------标准输出----------------------------")
'''
name=input("name：")
age=int (input("age："))
Job=input("Job:")
salary=float(input("salary:"))
'''
name="water"
age=14
Job="it"
salary=1500

print("%12ld" %(salary))


print("-标准输出1----------------------------")
info="""
    -----------info of %s-----------
    name:%s
    age:%d
    Job:%s
    salary:%f
    -------------------------------
""" %(name,name,age,Job,salary)
print(info)
print("-标准输出2----------------------------")
info="""
    -----------info of %s-----------
    name:%s
    age:%d
    Job:%s
    salary:%f
    -------------------------------
""" %(name,name,age,Job,salary)
print(info)

print("------------------getpass()方法----------------------------")
import getpass
#pwd=getpass.getpass("")

print("------------------sys模块----------------------------")
from sys import argv
from sys import getsizeof
print(getsizeof("1"))


print("------------------os模块----------------------------")
import os
print(os.system('pwd'))