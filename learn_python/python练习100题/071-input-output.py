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
题目：编写input()和output()函数输入，输出5个学生的数据记录。
程序分析：无。
'''

N = 3
#stu
#num : string
#name : string
#score[4] : list

student = []
for i in range(5):
    student.append(['','',[]])

def input_stu(stu):
    for i in range(N):
        stu[i][0] = raw_input('input student num:\n')
        stu[i][1] = raw_input('input stdent name:\n')
        for j in range(3):
            stu[i][2].append(int(raw_input('score:\n')))

def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' %(stu[i][0],stu[i][1]))
        for j in range(3):
            print('%-8'%stu[i][2][j])

if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)