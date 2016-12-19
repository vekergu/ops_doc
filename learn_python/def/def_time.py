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

#----------------------------对模块计时---------------------------------------
import time,sys
reps = 1000
repslist = range(reps)

def timer(func,*pargs,**kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs,**kargs)
    elapsed = time.clock() - start
    return (elapsed,ret)


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist ]

def mapCall():
    return list(map(abs,repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)

for test in (forLoop,listComp,mapCall,genExpr,genFunc):
    elapsed,result = timer(test)
    print ('-' * 33)
    print('%-9s: %.5f => [%s.....%s]' %(test.__name__,elapsed,result[0],result[-1]))





