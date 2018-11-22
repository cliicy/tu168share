# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy import Selector
from crawl_tu.pipelines import jgy_coll


class JgySpider(scrapy.Spider):
    name = "jgy"
    urls = ["http://www.jgy.com/"]
    download_delay = 3
    use_phantomjs = False
    start_urls = urls

    def parse(self, response):
        list=response.xpath('//*[@class="news-cont"]//ul//li').extract()
        for text in list:
            ybdd = {}
            sel = Selector(text=text)
            ybdd['link'] = sel.xpath('//div[@class="news-list"]//dl//dt/a/@href').extract()[0]
            ybdd['title'] = sel.xpath('//div[@class="news-list"]//dl//dt/a//text()').extract()[0]
            ybdd['zhaiyao'] = sel.xpath('//div[@class="news-list"]//dl//dd//text()').extract()[0]
            ybdd['author'] = sel.xpath('//div[@class="news-list"]//div[@class="time-author"]//text()').extract()[0]
            ybdd['time'] = sel.xpath('//div[@class="news-list"]//div[@class="time"]//text()').extract()[0]
            imgp = sel.xpath('//a/img').extract()[0]
            selp = Selector(text=imgp)
            ybdd['picsrc'] = selp.xpath('//img//@data-original').extract()[0]

            jgy_coll.update({'link': ybdd['link']},
                           {'$set': {'link': ybdd['link'], 'picsrc': ybdd['picsrc'], 'title': ybdd['title'],
                                     'zhaiyao': ybdd['zhaiyao'], 'author': ybdd['author'],
                                     'time': ybdd['time']}}, True)
        # for text in list:
        #     sel = Selector(text=text)
        #     link = sel.xpath('//dl//dt/a/@href').extract()
        #     title = sel.xpath('//dl//dt/a//text()').extract()
        #     zhaiyao = sel.xpath('//dl//dd//text()').extract()
        #     author = sel.xpath('//div[@class="time-author"]//text()').extract()
        #     time = sel.xpath('//div[@class="time"]//text()').extract()
        #     print(link, title, zhaiyao, author, time)



