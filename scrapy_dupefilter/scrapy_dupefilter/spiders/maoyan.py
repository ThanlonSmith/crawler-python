# -*- coding: utf-8 -*-
import scrapy

from scrapy.dupefilters import RFPDupeFilter


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/6']

    def parse(self, response):
        print(response)
        content_list = response.xpath('//dd')
        for item in content_list:
            text = item.xpath('.//p[@class="name"]//a/text()').extract_first()
            print(text)
        page_list = response.xpath('//ul[@class="list-pager"]/li/a/@href').extract()
        for page in page_list:
            from scrapy.http import Request
            page = 'https://maoyan.com/board/6' + page
            if 'javascript:void(0);' in page:
                page = 'https://maoyan.com/board/6'
            print(page)
            '''
            https://maoyan.com/board/6?offset=10
            '''
            yield Request(url=page, callback=self.parse)
        '''
        访问过的就不再请求了
        yield Request的时候，会先执行   
        def request_seen(self, request):
            fp = self.request_fingerprint(request)#将url(request)转换成md5值，fp就是url的md5值
            if fp in self.fingerprints:#fingerprints是一个集合，不能重复
                return True#表示已经访问过了
            #未访问过，把fp加进集合了
              self.fingerprints.add(fp)#如果
            if self.file:#如果有文件也会把访问记录写到文件中
                self.file.write(fp + os.linesep)
        '''
