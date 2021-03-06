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
# -*- coding: utf-8 -*-
from __future__ import print_function
import requests
import yaml

from format_converter import converter

try:
    import json
except ImportError:
    import simplejson as json

class SaltAPI(object):
    __token_id = ''
    def __init__(self,url,username,password):
        self.__url = url.rstrip('/')
        self.__user = username
        self.__password = password

    def token_id(self):
        ''' user login and get token id '''
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        content = self.postRequest(params,prefix='/login')
        try:
            self.__token_id = content['return'][0]['token']
        except KeyError:
            raise KeyError

    def postRequest(self,obj,prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token': self.__token_id}
        req = requests.post(url,data=obj,headers=headers,verify=False)
        content = req.json()
        return content

    def list_all_key(self):
        params = {'client': 'wheel', 'fun': 'key.list_all'}
        self.token_id()
        content = self.postRequest(params)
        minions = content['return'][0]['data']['return']['minions']
        minions_pre = content['return'][0]['data']['return']['minions_pre']
        return minions,minions_pre

    def delete_key(self,node_name):
        params = {'client': 'wheel', 'fun': 'key.delete', 'match': node_name}
        self.token_id()
        content = self.postRequest(params)
        ret = content['return'][0]['data']['success']
        return ret

    def accept_key(self,node_name):
        params = {'client': 'wheel', 'fun': 'key.accept', 'match': node_name}
        self.token_id()
        content = self.postRequest(params)
        ret = content['return'][0]['data']['success']
        return ret

    def remote_noarg_execution(self,tgt,fun):
        ''' Execute commands without parameters '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun,'expr_form': 'list'}
        self.token_id()
        content = self.postRequest(params)
        ret = content['return'][0]
        return ret

    def remote_execution(self,tgt,fun,arg):
        ''' Command execution with parameters '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg,'expr_form': 'list'}
        self.token_id()
        content = self.postRequest(params)
        ret = content['return']
        return ret

    def target_remote_execution(self,tgt,fun,arg):
        ''' Use targeting for remote execution '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': 'nodegroup'}
        self.token_id()
        content = self.postRequest(params)
        jid = content['return'][0]['jid']
        return jid

    def deploy(self,tgt,arg):
        ''' Module deployment '''
        params = {'client': 'local', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg}
        self.token_id()
        content = self.postRequest(params)
        return content

    def async_deploy(self,tgt,arg):
        ''' Asynchronously send a command to connected minions '''
        params = {'client': 'local_async', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg}
        self.token_id()
        content = self.postRequest(params)
        jid = content['return'][0]['jid']
        return jid

    def target_deploy(self,tgt,arg):
        ''' Based on the node group forms deployment '''
        params = {'client': 'local_async', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg, 'expr_form': 'nodegroup'}
        self.token_id()
        content = self.postRequest(params)
        jid = content['return'][0]['jid']
        return jid

def main():
    sapi = SaltAPI(url='http://192.168.1.12:8000',username='nginx',password='nginx2016')
    #sapi.token_id()
    #print('list all key:',sapi.list_all_key())
    #sapi.delete_key('node01.qhxrl.com')
    #sapi.accept_key('test-01')
    #mm = sapi.deploy('python01.qhxrl.com',arg=['saltenv="base_init"','roles.common'])
    #mm_key = mm['return'][0]['python01.qhxrl.com'].keys()
    #for item in mm_key:
        #print(item)

    #yml = yaml.safe_dump(mm_key)
    #print(yml)
    #print(yaml.load(mm))

    #print(sapi.remote_noarg_execution('python01.qhxrl.com','test.ping'))
    #print(sapi.remote_noarg_execution('python01.qhxrl.com','test.ping'))
    print(sapi.remote_noarg_execution([u'search',u'python01.qhxrl.com'],'test.ping'))

   # print(sapi.remote_execution('*','cmd.run','ls'))

if __name__ == '__main__':
    main()


