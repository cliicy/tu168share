# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from mycrawler.items import LinkItem
from scrapy import Selector
from scrapy import Request
from scrapy.http import Headers, HtmlResponse
from scrapy.selector import HtmlXPathSelector
from mycrawler.items import *
import sys
import time
import re
sys.path.append('../mycrawler')


class MySpider(scrapy.Spider):
    name = "yanbao"
    urls = ['http://data.eastmoney.com/report/']
    # urls = ['http://data.eastmoney.com/report/',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0y',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0z',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT00',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT01',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT02',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT03',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT04',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT05',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMA==',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMQ==',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMg==',
    #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMw==']
    # urls = []
    # for x in range(1,300):
    #     p=str(x)
    #     urls.append("http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&
    # js=var%20eNyUNdeY={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%
    # 22count%22:%22(count)%22}&ps=50&p="+p+"&mkt=0&stat=0&cmd=4&code=&rt=51330470")
    download_delay = 3
    use_phantomjs = False
    # allowed_domains = ["http://news.sina.com.cn/c/"]
    start_urls = urls

    def parse(self, response):
        data = LinkItem()
        # data['url'] = response.url
        data['content'] = response.body
        yield data

