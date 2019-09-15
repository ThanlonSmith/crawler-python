# -*- coding: utf-8 -*-
import scrapy


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['https://dig.chouti.com/']

    def parse(self, response):
        print(response.text)
