# -*- coding: utf-8 -*-
import scrapy


class QikeyishuSpider(scrapy.Spider):
    name = 'qikeyishu'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://cnblogs.com/']

    def parse(self, response):
        print(response)
