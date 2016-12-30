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

if __name__ == "__main__":
    class Student:
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = "c"
    a = Student()
    a.x = 3
    a.c = "a"

    f(a)
    print(a.x,a.c)