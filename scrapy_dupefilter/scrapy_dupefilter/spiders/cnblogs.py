# -*- coding: utf-8 -*-
import scrapy


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://cnblogs.com/']  # 内部是做了重定向

    def parse(self, response):
        print(response.request.url)
