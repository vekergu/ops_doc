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
import requests
import urllib2
import urllib
import json
import pprint
url = 'http://192.168.1.12:8000/'
login_url = 'http://192.168.1.12:8000/login'

auth_json = {'username': 'nginx', 'password': 'nginx2016', 'eauth': 'pam'}

#---------------------get URL----------------------------------
response = requests.get(url)
print(response.status_code)
print(response.content)

#-------------------post URL get token-----------------------------------
response = requests.post(login_url,json=auth_json)
print(response.status_code)
print(response.content)

content = eval(response.content)
print(type(content))

token = content['return'][0]['token']

#--------------------post URL  test.ping------------------------------------
'''
% curl -si http://192.168.1.12:8000 \
        -H "Accept: application/x-yaml" \
        -H "X-Auth-Token: bf1436122d2e9cd7b216922678b62646033de535" \
        -d client=local \
        -d tgt='*' \
        -d fun='test.ping' \
        -d arg
'''
cmd_json = {'client': 'local', 'tgt': 'python01.qhxrl.com', "fun": "test.ping"}
headers_json = {'Accept': 'application/json','X-Auth-Token': token}

response = requests.post(url,data=cmd_json,headers=headers_json)

print(response.status_code)
print(response.content)
'''
encode = urllib.urlencode(cmd_json)
obj = urllib.unquote(encode)
req = urllib2.Request(url, obj, headers_json)
opener = urllib2.urlopen(req)
print(opener.read())
'''

