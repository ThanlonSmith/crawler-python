# -*- coding: utf-8 -*-
import scrapy


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://cnblogs.com/']

    def parse(self, response):
        print(response.request.url, response.meta)
        '''
         response.meta = {
            'download_timeout': 180.0,
            'download_slot': 'cnblogs.com',
            'download_latency': 0.07253193855285645,
            'redirect_times': 1,
            'redirect_ttl': 19,
            'redirect_urls': ['http://cnblogs.com/'],
            'redirect_reasons': [301]
        }
        '''
        print(response.request.url, response.meta.get('depth'))  # meta中是没有depth,所以或取到的是None
