# -*- coding: utf-8 -*-
import scrapy


class BlueflagsSpider(scrapy.Spider):
    name = 'blueflags'
    allowed_domains = ['blueflags.cn']
    start_urls = ['http://www.blueflags.cn/']

    def parse(self, response):
        print(response.text)
