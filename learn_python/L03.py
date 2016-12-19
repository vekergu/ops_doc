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

#----------------------generator----------------------------------------------
def foo():
    for i in range(10):
        yield i

re = foo()
for item in re:
    print('item:',item)



print(xrange(10))
for item in xrange(10):
    print(item)


#----------------------file  迭代输出--------------------------------

f = open('e:\temp.txt','w')
f.write("aaadj\nsdjflsf\nsjflsjfkl\nsjdflj\n")
f.close()

def readLindes():
    seek = 0
    while True:
        with open('f:\temp.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return

f = readLindes()
print(f.next())
print(f.next())
for item in readLindes():
    print(item)


#---------------三元运算-----------------------------------------------
result = 'gt' if 1>3 else "lt"

#----------------lambda ------------------------------------------------
print((lambda x,y:x+y)(4,10) )

#----------------内置函数 ---------------------------------------------
a = []
#help(a)

print("dir:",dir())
print(vars())
print(type(a))
print(id(a))
print(pow(2,10))
print(2**10)


#www.cnblogs.com/wupeiqi/articles/4276448.html

#asiic 编码转化，可以随机生成字母
print(chr(68))
#16进制
print(hex(25))
#8进制
print(oct(13))
print(bin(2))
#
for k,v in enumerate(range(1,10,2),1):
    print(k,v)

#
def Function(arg):
    print(arg)

#通过apply来调用函数
#print(apply(Function,[1,2]))
print(map(lambda x:x+1,[1,2,3]))
print(filter(lambda x: x==1,[1,23,4]))

#--------------zip------------------------------
x = [1, 2, 3, 4]
y = [4, 5, 6]
z = [7, 8, 9, 10]
print(zip(x, y, z))

#----------------反射-----------------------
a = '8*8'
print(eval(a))

#------------------------以字符串的形式导入模块
temp = "os"
model = __import__(temp)
print(model.path)
#有3个模块，一个模块操作mysql，一个模块操作sqlserver
#一部分数据在mysql，一部分在sqlserver
#sqlserver宕机了，所以要把联系sqlserver的模块改为mysql
#和super的作用一至

#----------------------以字符串的形式执行函数
def conut():
    return 2
func = "path"
function = getattr(model, func)


#-------------------------常用模块-----------------------
#随机数
import random
print(random.random())
print(random.randint(1, 2))
print(random.randrange(1, 10))

#生成验证码
temp = random.randint(65,90)
print(chr(temp))

mm = map(chr,[random.randint(65,90) for i in range(1,5)])
print("".join(mm))
print('The value of PI is approximately {r}.'.format(r = "abc"))

#------------------------------MD5 加密-----------------
import hashlib
hash = hashlib.md5()
hash.update('admin')
print(hash.hexdigest())

#-----------------------------序列化 json------------------
import pickle
data = {'k1':123,'k2':"hello"}
li = ['alex',11,22,'ok','sb']
#pickle.dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)
p_list = pickle.dumps(data)
print(p_list)

p_pik = pickle.loads(p_str)
print(p_pik)

pickle.dump(li,open("/tmp/test.pk",'w'))
result = pickle.load(open("/tmp/test.pk",'r'))
print(result)

#json
import json
j_str = json.dumps(data)
print(j_str)

with open('/tmp/result.json','w') as fp:
    json.dump('data',fp)