# -*- coding: utf-8 -*-
class Sd1(object):
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        return s

    def process_spider_input(self, response, spider):
        '''
        :param response:下载器帮助我们下载下来的结果，是经过所有下载中间件的process_response,
        然后交给下一个process_spider_input。都执行完成后，交给回调函数。回调函数可以yield item
        或yield Request,当yield之后就会调用process_spider_output
        :param spider:
        :return:
        '''
        return None

    def process_spider_output(self, response, result, spider):
        '''
        所以process_spider_output有两个参数
        :param response:上一次下载的结果
        :param result:yield新的Request()对象
        :param spider:
        :return:
        '''
        for i in result:  # yield item或yield Request之后还可以再yield一个个返回,间接一个个返回
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    # 只在爬虫启动时执行一次
    def process_start_requests(self, start_requests, spider):
        # Must return only requests (not items).
        for r in start_requests:
            yield r


class Sd2(object):

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r
