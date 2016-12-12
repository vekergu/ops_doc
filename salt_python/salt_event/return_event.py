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
altstack的master上minion连接较多，下面这个程序可以分析哪些minion任务执行成功，哪些执行失败以及哪些没有返回

'''
import salt.utils.event
import re
import signal, time
import sys
import os
def single_handler(target):
    os.execl('/usr/bin/salt', 'salt', target, 'state.sls', 'os')

def handler(num1, num2):
    #signal.signal(signal.SIGCLD,signal.SIG_IGN)
    print 'We are in signal handler'
    print 'Job Not Ret: '+str(record[jid])
    print ' Job Failed: '+str(failedrecord[jid])
    print 'all done...'
    for item in failedrecord[jid]:
        #print item
        try:
           pid  = os.fork()
           if pid == 0:
              single_handler(item)
        except OSError:
           print 'we exec. '+ item +' error!'
    for item in record[jid]:
        #print item
        try:
           print 'fork ok ' + item
           pid = os.fork()
           if pid == 0 :
              single_handler(item)
        except OSError:
           print 'we exec. '+item + ' error!'
    sys.stdout.flush()
    os._exit(0)



fd = open('/tmp/record', 'w+')
#sys.stdout = fd
#sys.stderr = fd

signal.signal(signal.SIGCLD, handler)

#fd = open('/var/log/record', 'w+')
os.dup2(fd.fileno(), sys.stdout.fileno())
os.dup2(fd.fileno(), sys.stderr.fileno())

#sys.stdout = fd
#sys.stderr = fd


try:
   pid = os.fork()
   if pid == 0:
      time.sleep(2)
      try:
         os.execl('/usr/bin/salt', 'salt', '*', 'state.sls', 'os')
      except OSError:
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
    eachevent=dict(eachevent)
    result = reg.findall(eachevent['tag'])
    if not flag and result:
       flag = True
       jid = result[0]
       print "   job_id: " + jid
       print "  Command: " + dict(eachevent['data'])['fun'] + ' ' + str(dict(eachevent['data'])['arg'])
       print "    RunAs: " + dict(eachevent['data'])['user']
       print "exec_time: " + dict(eachevent['data'])['_stamp']
       print "host_list: " + str(dict(eachevent['data'])['minions'])
       sys.stdout.flush()
       record[jid]=eachevent['data']['minions']
       failedrecord[jid]=[]
       reg1 = re.compile('salt/job/'+jid+'/ret/([0-9.]+)')
    else:
       result = reg1.findall(eachevent['tag'])
       if result:
          record[jid].remove(result[0])
          if not dict(eachevent['data'])['success']:
             failedrecord[jid].append(result[0])
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