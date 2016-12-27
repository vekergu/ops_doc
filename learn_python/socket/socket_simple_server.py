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
import socket

ip_port = ("192.168.1.42",8000)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    print('server waiting...')
    conn,addr = sk.accept()

    client_data = conn.recv(1024)
    print(client_data)
    conn.sendall('不要回答,不要回答,不要回答')

    conn.close()