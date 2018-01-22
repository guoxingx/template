# coding: utf-8

from scrapy import Spider


def create_spider(name, processor=None, *urls):
    def parse(self, response):
        if processor:
            processor(response)
    spider_class = type(
        '{}Spider'.format(name),
        (Spider,),
        {'name': name, 'start_urls': urls, 'parse': parse}
    )
    return spider_class
