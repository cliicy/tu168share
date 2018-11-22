#-*- coding:utf-8 -*-

import os
import urllib
from urllib import request
from lxml import etree

class Spider:
    def __init__(self):

        self.ua_header = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

    def loadPage(self, url):
        response = request.urlopen(url)
        html = response.read()
        html = html.decode("utf-8")
        selector = etree.HTML(html)


        xx = selector.xpath('//*[@class="news-cont"]//ul//li//div[@class="news-list"]//text()')
        for x in xx:
            print(x)

        # 这个地方自己写规则


#模拟__main__函数：
if __name__ == '__main__':
    #首先创建爬虫对象
    mySpider = Spider()
    #调用爬虫对象的方法，开始工作
    mySpider.loadPage("http://jgy.com/")