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

import re
event = {'tag': 'salt/job/20161205133611061488/new', 'data': {'tgt_type': 'glob', 'jid': '20161205133611061488', 'tgt': '*', '_stamp': '2016-12-05T05:36:11.062732', 'user': 'root', 'arg': ['20161205133606045481'], 'fun': 'saltutil.find_job', 'minions': ['node01.qhxrl.com', 'compute1.qhxrl.com', 'controller.qhxrl.com', 'haproxy01.qhxrl.com', 'node02.qhxrl.com', 'saltstack02-xen.qhxrl.com', 'sz-a-dns01-xen.qhxrl.com', 'sz-a-qhfaxlvs01-master-xen.qhfax.com', 'file01.qhfax.com', 'node03.qhxrl.com', 'python01.qhxrl.com']}}
string = event['tag']
str = "new"
def get_JID(string,str):
    if  string.find(str) != "-1" :
        str_list = string.split("/")
        #print str_list
        JID = str_list[2]
        #print JID
    return JID

print get_JID(string,str)

