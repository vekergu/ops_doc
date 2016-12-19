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
import yaml
from salt_api.saltapi_demo01 import SaltAPI

class saltJob():
    def __init__(self,tgt = []):
        self.sapi = SaltAPI(url='http://192.168.1.12:8000',username='nginx',password='nginx2016')
        self.tgt = tgt
        self.num_tgt = len(tgt)
    def list_all_key(self):
        result = self.sapi.list_all_key()
        return result
    def test_ping(self):
        text = ""
        su_num = 0
        result = self.sapi.remote_noarg_execution(tgt=self.tgt,fun="test.ping")
        for item,value in result.items():
            if value:
                su_num += 1
            re = "{0}  {1}".format(item,value)
            text = "{0}\n{1}".format(text,re)
        text = "{0}\n--------------------\ntotal:{1}\nsuceful:{2}\nunsuceful:{3}".format(text,self.num_tgt,su_num,self.num_tgt - su_num)
        return text
    def cmd_run(self,tgt,arg):
        re = ""
        result = self.sapi.remote_execution(fun="cmd.run",arg=arg)
        for host_name,value in result[0].items():
            text = "----------{0}-----------\n{1}".format(host_name,value)
            re = "{0}\n{1}".format(text,re)
        return re

def main():
    temp = saltJob([u'search',u'python01.qhxrl.com'])
    #print(temp.test_ping())
    print(temp.list_all_key())
    #print(temp.cmd_run("df -h"))

if __name__ == "__main__":
    main()


