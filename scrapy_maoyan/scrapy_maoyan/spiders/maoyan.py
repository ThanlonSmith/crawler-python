# -*- coding: utf-8 -*-
import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/6']

    def parse(self, response):
        '''
         爬虫爬完起始url，自动执行该函数
        :param response:对象，封装了所有响应相关的数据，比如响应头、响应体
        :return:None
        '''
        content_list = response.xpath('//dd')
        f = open('new.log', mode='a+')
        for item in content_list:
            text = item.xpath('.//p[@class="name"]//a/text()').extract_first()
            print(text)
            f.write(text.strip() + '\n')
        f.close()
        page_list = response.xpath('//ul[@class="list-pager"]/li/a/@href').extract()
        # ['javascript:void(0);', '?offset=10', '?offset=20', '?offset=30', '?offset=40', '?offset=10']
        for page in page_list:
            from scrapy.http import Request
            page = 'https://maoyan.com/board/6' + page
            if 'javascript:void(0);' in page:
                page = 'https://maoyan.com/board/6'
            print(page)
            '''
            https://maoyan.com/board/6?offset=10
            '''
            yield Request(url=page, callback=self.parse)  # 通知scrapy再次向新的地址发送请求
