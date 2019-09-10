# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyPipelineItem(scrapy.Item):  # 类名不是写死的，可自定义
    href = scrapy.Field()
    title = scrapy.Field()
