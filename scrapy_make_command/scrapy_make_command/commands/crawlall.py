# -*- coding: utf-8 -*-
from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        '''
        语法支持,命令的提示,scrapy crawlall --help
        :return:
        '''
        return '[options]'

    def short_desc(self):
        '''
        命令的介绍,可通过crapy --help
        :return:
        '''
        return 'Run all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()  # 找到所有爬虫
        # print(spider_list)
        for name in spider_list:  # 找到爬虫后循环这两个爬虫
            self.crawler_process.crawl(name, **opts.__dict__)  # 添加两个爬虫任务
        self.crawler_process.start()
