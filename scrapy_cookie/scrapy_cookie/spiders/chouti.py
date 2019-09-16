# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.http import Request
from urllib.parse import urlencode


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['https://dig.chouti.com']
    cookie_dict = {}

    def parse(self, response):
        print(response)
        '''
              第一次访问抽屉的时候返回的内容response
              :param response:
              :return:
        '''
        '''
        去响应头中获取cookie
        '''

        # 去响应头中获取cookie,cookie保存在cookie_jar对象
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        for i, v in cookie_jar._cookies.items():
            print(i, v)
        # 去对象中将cookie解析到字典
        for k, v in cookie_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value
        # print(cookie_dict)
        yield Request(
            url='https://dig.chouti.com/login',
            method='POST',
            body='password=123456&loginType=2&phone=%2B8618512152005&NECaptchaValidate=54qajoVtRONV-Pbu87QdaDAK2XjYVi-HdWYP8emDquaYO7N1Felra4dWFa5uzV6J0tHE5u74PMCmpKrBxJgwhsObcoT1ufv5BkbSub6f4kLxXfUx5WdSxTjZ7K2YPFR1HSpIQnWVr6OXq2fWdJ7C.MeVCvGscNXkX-t4DHKp8gbGtT9SZKA07zefpl101iRG0hmPNK.xBQViXsGPZAS2f.vLWVa8PXPbZ.Y-.uwGfzXCcF5F8UfT8vcIZF7Co1kJ9Bgo-82mLyyt4v6sFfWjUx_NvChvngrSy1ujoHAFTreiXNswonNkcNfCWMOGHRzAxMjGDqtzgdMmf1e55NWCRiAw-dZwSue.ERa8MXQeHIGtnQ-lJASGlWA6JolrmWGEovLrG.Ctrpk6d40xLk0EETzOb067taEoHvZGnLi2Y4tPc00qgA0iKYbKVQp7YbMSP2OKcxI-zReaEwDAVCNKLuBj7fUCP04Sb4B1ozK_gnmAj7i72AE4KlskWPS3',
            # body=urlencode({
            #     'password': 2232323232,
            #     'loginType': 2,
            #     'phone': +8618512152001
            # }),
            cookies=self.cookie_dict,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            callback=self.check_login
        )

    def check_login(self, response):
        '''
        登录成功后的回调函数
        :param response:
        :return:
        '''
        print(response.text)
        yield Request(
            url='https://dig.chouti.com/',
            cookies=self.cookie_dict,
            callback=self.index
        )

    def index(self, response):
        news_list = response.xpath('//div[@id="content-list"]/div[@class="item"]')
        for new in news_list:
            link_id = new.xpath('.//div[@class="part2"]/@share-linked').extract_first()
            yield Request(
                url='http://dig.chouti.com/link/vote?linksId=%s' % (link_id),
                method='POST',
                cookies=self.cookie_dict,
                callback=self.check_result
            )
        page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        for page in page_list:
            page = 'https://dig.chouti.com' + page
            yield Request(url=page, callback=self.index)  # 翻页点赞

    def check_result(self, response):
        print(response.text)
