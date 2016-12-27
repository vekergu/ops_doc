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
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

#year  month  day
#润年多一天
#365  或  366 天
'''
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum = sum + day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)
'''
#-------------standarad  function------------------------------

def  std_days(str_data):
    year = int(str_data.split("-")[0])
    month = int(str_data.split("-")[1])
    day = int(str_data.split("-")[2])

    months = (0,31,59,90,120,151,181,212,243,273,304,334)
    if 0 < month <= 12:
        sum = months[month - 1]
    else:
        print('data error')
    sum = sum + day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    return sum


print(std_days("2015-01-25"))

#--------------unit test---------------------------------
import unittest

class TestStdDays(unittest.TestCase):
    def test_init(self):
        self.assertEqual(std_days("2015-01-25"),25)
        self.assertTrue(isinstance(std_days("2015-01-25"),int))


if __name__ == '__main__':
    unittest.main()