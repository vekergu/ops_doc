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

import logging
import paramiko
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class SFTPClient(object):
    def __init__(self,hostname,user,password,root,port=22):
        self.root = root
        self.ssh = paramiko.SSHClient()
        #设置key策略，自动添加
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=hostname,port=port,username=user,password=password)
        self.sftp = self.ssh.open_sftp()
        #切换到root的目录
        self.sftp.chdir(self.root)

    def create_dir(self,path):
        self.sftp.mkdir(path)

    def put(self,src,dst):
        self.sftp.put(src.dst)

    def close(self):
        self.ssh.close()

class BackupWatchEventHandler(PatternMatchingEventHandler):
    def __init__(self,sftp,patterns=None,ignore_patterns=None,case_sensitive=False):
        super(BackupWatchEventHandler,self).__init__(patterns=patterns,
                                                         ignore_patterns=ignore_patterns,
                                                         ignore_directories=False,
                                                         case_sensitive=case_sensitive)
        self.sftp = sftp

    def on_created(self, event):
        if event.is_directory:
            self.sftp.create_dir(event.src_path)
        else:
            self.sftp.put(event.src_path,event.src_path)

    def on_modified(self,event):
        if not event.is_directory:
            self.sftp.put(event.src_path,event.src_path)

    def on_moved(self,event):
        self.sftp.move(event.src_path,event.dest_path)

    def on_any_event(self,event):
        logging.info("event {0} of {1}".format(event.event_type,event.src_path))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    sftp = SFTPClient('192.168.1.46','root','password','/tmp')
    handler = BackupWatchEventHandler(sftp)
    observer = Observer()
    observer.schedule(handler,".",recursive=True)
    observer.start()

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    sftp.close()








