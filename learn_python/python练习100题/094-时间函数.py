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
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
'''

import time
import random

play_it = raw_input('do you want to play it.(\'y\' or \'n\')')
while play_it == "y":
    c = raw_input('input a character:\n')
    i = random.randint(0,2**32) % 100
    print('please input number you guess:\n')
    start = time.clock()
    guess = int(raw_input('input you gess:\n'))
    while guess != i:
        if guess > i:
            print("大了")
            guess = int(raw_input('input your guess:\n'))
        else:
            print('小了')
            guess = int(raw_input('input your guess:\n'))
    end = time.clock()
    b = time.time()

    var = (end - start) / 18.2
    print(end - start)

    if var < 15:
        print('you are very clever！')
    elif var < 25:
        print('you are normal!')
    else:
        print('you are stupid!')

    print('Congradulations')
    print('The number you guess is %d' %i)
    play_it = raw_input('do you want to play it.')