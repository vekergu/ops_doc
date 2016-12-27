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
题目：暂停一秒输出。
程序分析：无。
'''
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime( time.localtime(time.time()) ))
print("now time",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) )
print("now time",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
time.sleep(1)
print(time.time())
print("end time",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )