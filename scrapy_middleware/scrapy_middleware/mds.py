# -*- coding: utf-8 -*-
from scrapy.http import HtmlResponse, Request


class Mds1(object):
    @classmethod
    def from_crawler(cls, crawler):
        '''
        如果有这个方法可以自己创建对象，如果没有可以自己创建对象
        :param crawler:
        :return:
        '''
        # This method is used by Scrapy to create your spiders.
        s = cls()
        return s

    def process_request(self, request, spider):
        print('Mds1.process_request', request)
        '''
        1. 返回Response
        '''
        # return HtmlResponse(url='www.xxx.com', status=200, headers=None, body=b'thanlon')
        import requests
        # ret = request.get(request.url)  # ret.content是字节
        # return HtmlResponse(url=request.url, status=200, headers=None, body=ret.content)  # 告诉去请求的地址下载了,但结果是自己伪造的
        '''
        2. 返回request
        '''
        # return Request('https://www.cnblogs.com/qikeyishu/')#自己一个请求自己
        '''
        3. 抛出异常,把请求丢弃掉,可以抛出异常
        '''
        # from scrapy.exceptions import IgnoreRequest
        # raise IgnoreRequest
        '''
        4. 对请求进行加工
        '''
        request.hraders[
            'USER_AGENT'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'

    def process_response(self, request, response, spider):
        print('Mds1.process_response', response)
        return response

    def process_exception(self, request, exception, spider):
        pass


class Mds2(object):
    @classmethod
    def from_crawler(cls, crawler):
        '''
        如果有这个方法可以自己创建对象，如果没有可以自己创建对象
        :param crawler:
        :return:
        '''
        # This method is used by Scrapy to create your spiders.
        s = cls()
        return s

    def process_request(self, request, spider):
        print('Mds2.process_request', request)
        return None

    def process_response(self, request, response, spider):
        print('Mds2.process_response', request, response)
        return response

    def process_exception(self, request, exception, spider):
        pass
