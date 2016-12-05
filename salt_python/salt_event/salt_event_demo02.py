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
import salt.utils.event
import re
import signal, time
import sys
#{'tag': 'salt/job/20151202210437808909/new', 'data': {'tgt_type': 'glob', 'jid': '20151202210437808909', 'tgt': '*', '_stamp': '2015-12-02T21:04:37.809305', 'user': 'root', 'arg': ['routetable'], 'fun': 'grains.item', 'minions': ['172.18.1.212', '172.18.1.214', '172.18.1.213', '172.18.1.211']}}
#{'tag': 'salt/job/20151202210437808909/ret/172.18.1.213', 'data': {'fun_args': ['routetable'], 'jid': '20151202210437808909', 'return': {'routetable': 'Not Show'}, 'retcode': 0, 'success': True, 'cmd': '_return', '_stamp': '2015-12-02T21:04:37.827085', 'fun': 'grains.item', 'id': '172.18.1.213'}}
import os

def handler(num1, num2):
    signal.signal(signal.SIG_IGN, handler)
    print 'We are in signal handler'
    print 'Job Not Ret: '+str(record[jid])
    print ' Job Failed: '+str(failedrecord[jid])
    for item in failedrecord[jid]:
        os.system('salt '+ str(item) + ' state.sls os')
    for item in record[jid]:
        os.system('salt '+ str(item) + ' state.sls os')
    os._exit(0)

signal.signal(signal.SIGCLD, handler)

#fd = open('/var/log/record', 'a+')
#os.dup2(fd.fileno(), sys.stdout.fileno())
#os.dup2(fd.fileno(), sys.stderr.fileno())

try:
   pid = os.fork()
   if pid == 0:
      time.sleep(2)
      try:
         os.execl('/usr/bin/salt', 'salt', '*', 'state.sls','salt_env="base_init"', 'roles.common')
      except:
         print 'exec error!'
         os._exit(1)
except OSError:
   print 'first fork error!'
   os._exit(1)

event = salt.utils.event.MasterEvent('/var/run/salt/master')
flag=False
reg=re.compile('salt/job/([0-9]+)/new')
reg1=reg
#a process to exec. command, but will sleep some time
#another process listen the event
#if we use this method, we can filter the event through func. name
record={}
failedrecord={}
jid = 0


#try:
for eachevent in event.iter_events(tag='salt/job',full=True):
    #time.sleep(20)
    #print eachevent
    #print "------"
    eachevent=dict(eachevent)
    #print eachevent
    result = reg.findall(eachevent['tag'])
    if not flag and result:
       flag = True
       #record = {}
       #failedrecord = {}
       jid = result[0]
       print "   job_id: " + jid
       print "  Command: " + dict(eachevent['data'])['fun'] + ' ' + str(dict(eachevent['data'])['arg'])
       print "    RunAs: " + dict(eachevent['data'])['user']
       print "exec_time: " + dict(eachevent['data'])['_stamp']
       print "host_list: " + str(dict(eachevent['data'])['minions'])
       record[jid]=eachevent['data']['minions']
       failedrecord[jid]=[]
       reg1 = re.compile('salt/job/'+jid+'/ret/([0-9.]+)')
       #print jid
    else:
       result = reg1.findall(eachevent['tag'])
       #print result.group(0)
       if result:
          record[jid].remove(result[0])
          if not dict(eachevent['data'])['success']:
             #print result[0]
             #record[jid].remove(result[0])
             #print 'Job Not Ret: '+str(record[jid])
             #print ' Job Failed: '+str(failedrecord[jid])
             #if not record[jid]:
             #   break
             failedrecord[jid].append(result[0])
             #print ' Job Failed: '+str(failedrecord[jid])
          #else:
             #failedrecord[jid].append(result[0])
             #print 'Job Not Ret: '+str(record[jid])
#except:
#   print 'we in except'
"""
   print 'Job Not Ret: '+str(record[jid])
   print ' Job Failed: '+str(failedrecord[jid])
   for item in failedrecord[jid]:
       os.system('salt '+ str(item) + ' state.sls os')
   for item in record[jid]:
       os.system('salt '+ str(item) + ' state.sls os')
   os._exit(0)
"""
#print 'Job Not Ret: '+str(record[jid])
#print ' Job Failed: '+str(failedrecord[jid])
"""
if fnmatch.fnmatch(eachevent['tag'], 'salt/job/*/new'):
print eachevent['data']['minions']
elif fnmatch.fnmatch(eachevent['tag'], 'salt/job/*/ret/*'):
print eachevent['data']['jid']
print eachevent['data']['return']
"""