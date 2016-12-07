#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 顾少
#        Email: vekergu@163.com
#     HomePage: https://github.com/vekergu
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================
#import builtin
import signal

#import salt
import salt.utils.event

event = salt.utils.event.MasterEvent('/var/run/salt/master')

class SaltEvent():
    def __init__(self,salt_event):
        self.salt_event = salt_event
        self.salt_tag = self.salt_event['tag']

    def get_jid(self):
        if_job = self.salt_tag.find("job")
        if_new = self.salt_tag.find("new")

        if if_new  != -1 and if_job != -1:
            #print if_new,if_job
            str_list = self.salt_tag.split("/")
            jid = str_list
            return jid[2]
        return None
    def std_info(self):
        jid = self.get_jid()
        if jid:
            print jid,self.salt_event['data']['tgt'],self.salt_event['data']['fun'],self.salt_event['data']['arg']

    def get_minion(self):
        return self.salt_event['data']




for eachevent in event.iter_events(full=True):
    signal.signal(signal.SIGCLD, SaltEvent)
    job_event = SaltEvent(eachevent)
    job_event.std_info()