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

from math import sqrt
def is_prime(n):
    if n == 0 or n ==1:
        return False
    for i in range(int(sqrt(n))+1):
        if n%2 == 0:
            return False
    return True
