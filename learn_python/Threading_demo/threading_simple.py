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

import threading
import time

def show(arg):
    time.sleep(1)
    print('thread'+str(arg))

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread stop')
'''

    start            线程准备就绪，等待CPU调度
    setName      为线程设置名称
    getName      获取线程名称
    setDaemon   设置为后台线程或前台线程（默认）
                       如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止
                        如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
    join              逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
    run              线程被cpu调度后自动执行线程对象的run方法

'''