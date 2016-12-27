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


print("-------------------Logger，Handler，Formatter，Filter的实例-------------------")
# 创建一个logger
#默认的日志级别WARNIING
logger = logging.getLogger()

#原来logger1和logger2对应的是同一个Logger实例
#如果logger2进行设置变更，就会影响到logger1
logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('mylogger.child1')
logger3.setLevel(logging.WARNING)

logger4 = logging.getLogger('mylogger.child1.child2')
logger4.setLevel(logging.DEBUG)

logger5 = logging.getLogger('mylogger.child1.child2.child3')
logger5.setLevel(logging.DEBUG)

print("---------------创建一个handler，用于写入日志文件")
fh = logging.FileHandler('/tmp/test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#定义一个filter
#filter = logging.Filter('mylogger.child1.child2')
#fh.addFilter(filter)

# 给logger添加handler
#logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)

#logger1.addFilter(filter)
logger1.addHandler(fh)
logger1.addHandler(ch)

logger2.addHandler(fh)
logger2.addHandler(ch)

#logger3.addFilter(filter)
logger3.addHandler(fh)
logger3.addHandler(ch)

#logger4.addFilter(filter)
logger4.addHandler(fh)
logger4.addHandler(ch)

logger5.addHandler(fh)
logger5.addHandler(ch)

# 记录一条日志
print("---------------logger")
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
#结果输出了 WARNING及其级别以上的日志，debug，info日志没有输出


print("---------------logger1")
logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')
#结果没有出现debug日志

print("---------------logger2")
logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')

print("---------------logger3")
logger3.debug('logger3 debug message')
logger3.info('logger3 info message')
logger3.warning('logger3 warning message')
logger3.error('logger3 error message')
logger3.critical('logger3 critical message')

print("---------------logger4")
logger4.debug('logger4 debug message')
logger4.info('logger4 info message')
logger4.warning('logger4 warning message')
logger4.error('logger4 error message')
logger4.critical('logger4 critical message')

print("---------------logger5")
logger5.debug('logger5 debug message')
logger5.info('logger5 info message')
logger5.warning('logger5 warning message')
logger5.error('logger5 error message')
logger5.critical('logger5 critical message')


#为什么logger1、logger2对应的每个输出分别显示两次，logger3对应的输出显示3次，logger4对应的输出显示4次......呢？
'''
这是因为我们通过logger = logging.getLogger()显示的创建了root Logger，而logger1 = logging.getLogger('mylogger')创建了root Logger的孩子(root.)mylogger,logger2同样。
logger3 = logging.getLogger('mylogger.child1')创建了(root.)mylogger.child1
logger4 = logging.getLogger('mylogger.child1.child2')创建了(root.)mylogger.child1.child2
logger5 = logging.getLogger('mylogger.child1.child2.child3')创建了(root.)mylogger.child1.child2.child3
而孩子,孙子，重孙……既会将消息分发给他的handler进行处理也会传递给所有的祖先Logger处理。
'''


'''
有多中可用的Handler：
logging.StreamHandler 可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息
logging.FileHandler 用于向一个文件输出日志信息
logging.handlers.RotatingFileHandler 类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建一个新的同名日志文件继续输出
logging.handlers.TimedRotatingFileHandler 和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就自动创建新的日志文件
logging.handlers.SocketHandler 使用TCP协议，将日志信息发送到网络。
logging.handlers.DatagramHandler 使用UDP协议，将日志信息发送到网络。
logging.handlers.SysLogHandler 日志输出到syslog
logging.handlers.NTEventLogHandler 远程输出日志到Windows NT/2000/XP的事件日志
logging.handlers.SMTPHandler 远程输出日志到邮件地址
logging.handlers.MemoryHandler 日志输出到内存中的制定buffer
logging.handlers.HTTPHandler 通过"GET"或"POST"远程输出到HTTP服务器
'''
