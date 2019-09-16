# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    def start_requests(self):
        '''
        # 第一种方式
        # 引擎调用start_requests方法得到的是生成器,得到生成器后一个个拿到request对象,内部调用使用的是__next__方法
         for url in self.start_urls:
            yield Request(url=url)
        '''
        '''
        #第二种方式
        '''
        for url in self.start_urls:
            req_list = []
            req_list.append(Request(url=url))
            return req_list

    def parse(self, response):
        pass
