# coding: utf-8

import os
import xlrd

from scrapy.crawler import CrawlerProcess

from app.models import Spider as SpiderModel

from . import session
from .seeker import create_spider


def run_carbens_spider():
    url_data = load_data_from_files()
    spider = _create_carbens_spider(url_data)
    process = CrawlerProcess()
    process.crawl(spider)
    process.start()


def load_data_from_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = '{}/files/carbens.xlsx'.format(current_dir)
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]

    data = {}
    for i in range(table.nrows):
        url = table.cell(i, 4).value
        if url and 'http://' in url:
            data[url] = {
                'location': table.cell(i, 1),
                'name': table.cell(i, 2),
                'homepage': table.cell(i, 3),
                'url': url
            }
    return data


def _create_carbens_spider(url_data):
    urls = [url for url in url_data]

    def processor(response):
        print(response)
        if '碳'.encode() in response.body:
            url = response.url
            _save_info(response, url_data.get(url))
    name = 'Carbens'
    return create_spider(name, processor, *urls)


def _save_info(response, data):
    content = response.body
    s = SpiderModel(content=content, **data)
    session.add(s)
    session.commit()
