# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request


class QikeyishuSpider(scrapy.Spider):
    name = 'qikeyishu'
    allowed_domains = ['cnblogs.com']
    start_urls = (
        'https://www.cnblogs.com/',
    )

    def start_requests(self):
        '''
        自己定制起始url,如果没有写,url会使用默认的start_urls
        :return:
        '''
        url = 'https://www.cnblogs.com/qikeyishu/'
        yield Request(url=url, callback=self.parse, )

    def parse(self, response):
        print('response', response)  # response在中间件类执行process_response方法的时候有的
