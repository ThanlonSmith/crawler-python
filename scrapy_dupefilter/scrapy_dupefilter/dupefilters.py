# -*- coding: utf-8 -*-
from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint


class MyDupeFilter(BaseDupeFilter):
    def __init__(self):
        self.visted_fd = set()#这里只是放到集合中，其实是可以放到redis中的

    @classmethod
    def from_settings(cls, settings):
        '''
        内部会先检查有没有from_settings，如果有可以通过cls()拿到对象，如果没有自己实例化
        :param settings:
        :return:
        '''
        return cls()

    def request_seen(self, request):
        '''
        :param request:
        :return:# None表示都没有访问过,会再次访问,也就是没有去重
        '''
        fd = request_fingerprint(request=request)
        if fd in self.visted_fd:  # 如果在访问过的集合中
            return True
        self.visted_fd.add(fd)

    def open(self):  # can return deferred
        print('爬虫开始的时候')

    def close(self, reason):  # can return a deferred
        print('爬虫开始的时候')

    # def log(self, request, spider):  # 记录日志的
    #     print('日志')
