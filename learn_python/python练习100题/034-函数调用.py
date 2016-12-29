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

def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()