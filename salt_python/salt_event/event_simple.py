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
'''
as
 salt-run state.event


iter_events:    Creates a generator that continuously listens for events

'''
import salt.utils.event
event = salt.utils.event.MasterEvent('/var/run/salt/master')
for eachevent in event.iter_events(full=True):
    print eachevent
    print "------"