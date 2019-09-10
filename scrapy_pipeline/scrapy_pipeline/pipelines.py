# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem


class FilePipeline(object):  # 类名不是写死的，可自定义
    '''
    源码内容：
    第一步：
        判断当前ScrapyPipelinePipeline类中是否含有from_crawler，如果有
        obj = ScrapyPipelinePipeline.from_crawler(……)
        如果没有：
        obj = ScrapyPipelinePipeline()
    第二步：
        obj.open_spider(self, spider)
    第三步：
        obj.process_item(self, item, spider)、obj.process_item()，obj.process_item()……
    第四步：
        obj.close_spider(self, spider)
    '''

    def __init__(self, path):
        self.f = None
        self.path = path

    @classmethod
    def from_crawler(cls, crawler):  # cls是当前类
        '''
        初始化的时候用于创建pipeline对象(不用实例化就可以创建)
        :param crawler:
        :return:
        '''
        print('File.from_crawler')
        path = crawler.settings.get('HREF_FILE_PATH')  # 向所有的配置文件(自己的配置和内置的配置)找HREF_FILE_PATH
        return cls(path)

    def open_spider(self, spider):
        '''
        爬虫开始执行时调用
        :param spider:
        :return:
        '''
        if spider.name=='cnblogs':
            print('File.open_spider')
        self.f = open(self.path, 'a+')

    def process_item(self, item, spider):
        print('file', item['href'])
        self.f.write(item['href'] + '\n')
        # return item  # 交给下一个pipeline的process_item方法
        raise DropItem()

    def close_spider(self, spider):
        '''
        爬虫关闭时被调用
        :param spider:
        :return:
        '''
        print('File.close_spider')
        self.f.close()


class DbPipeline(object):  # 类名不是写死的，可自定义
    def __init__(self, path):
        self.f = None
        self.path = path

    @classmethod
    def from_crawler(cls, crawler):  # cls是当前类
        '''
        初始化的时候用于创建pipeline对象(不用实例化就可以创建)
        :param crawler:
        :return:
        '''
        print('Db.from_crawler')
        path = crawler.settings.get('HREF_DB_PATH')  # 向所有的配置文件(自己的配置和内置的配置)找HREF_FILE_PATH
        return cls(path)

    def open_spider(self, spider):
        '''
        爬虫开始执行时调用
        :param spider:
        :return:
        '''
        print('Db.open_spider')
        self.f = open(self.path, 'a')

    def process_item(self, item, spider):
        print('db', item['href'])
        self.f.write(item['href'] + '\n')
        return item

    def close_spider(self, spider):
        '''
        爬虫关闭时被调用
        :param spider:
        :return:
        '''
        print('Db.close_spider')
        self.f.close()
