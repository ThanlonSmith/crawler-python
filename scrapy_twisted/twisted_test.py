# -*- coding: utf-8 -*-
'''
teisted:是一个基于事件循环的异步非阻塞模块，简而言之：也就是一个线程同时可以向多个目标发送http请求
1、阻塞：不等待，请求发出去不用等待结果，而是继续法下一个连接请求。也就是发送一个连接，马上发下一个连接请求。
import socket
sk = socket.socket()
sk.setblocking(False)
sk.connect((1.2.3.4,80))

import socket
sk = socket.socket()
sk.setblocking(False)
sk.connect((1.2.3.4,80))
……
2、异步：体现在回调，拿到结果后才会（执行回调）通知请求者
回调函数：
def callback(contents):
    print(contents)
3、事件循环：循环检测，循环三个socket任务，检查其请求者的状态，是否连接成功，是否返回结果。
'''
from twisted.web.client import getPage, defer
from twisted.internet import reactor


# 第一部分：代理开始接收任务
def callback(contents):  # content:kiku
    pass


deferred_list = []  # 三个任务[(thanlon,kiku),(thanlon,yuqin)]
url_list = ['https://www.blueflags.cn/', 'https://segmentfault.com/', 'https://stackoverflow.com/']
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf-8'))
    deferred.addCallback(callback)  # 如果找到了，就告诉请求过来取
    deferred_list.append(deferred)
# 代理执行完任务后停止
dlist = defer.DeferredList(deferred_list)


def all_done(arg):
    reactor.stop()


dlist.addBoth(all_done)  # 不管成功与否，我都会停下来
# 第三部分：代理开始处理
reactor.run()
