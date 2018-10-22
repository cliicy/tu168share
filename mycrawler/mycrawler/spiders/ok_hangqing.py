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
    name = "dy_main"
    urls = [
        "https://www.okex.com/marketList#market=usdt",
        "https://www.okex.com/marketList#market=btc",
        "https://www.okex.com/marketList#market=eth",
        "https://www.okex.com/marketList#market=okb",
        # "https://www.okex.com/marketList#market=futures"
    ]
    download_delay = 5
    use_phantomjs = True
    #allowed_domains = ["http://news.sina.com.cn/c/"]
    start_urls = urls

    def parse(self, response):
        #print("@"*100,response.url)
        #print(response.body)
        list=response.xpath('//*[@class="market-list-tickers"]//table//tbody//tr').extract()
        for text in list:
            sel = Selector(text=text)
            #print("@"*100)
            #print(data)
            symbol_lower = sel.xpath('//@data-product').extract()
            symbol_nodisplay = sel.xpath('//@style').extract()
            symbol_power = sel.xpath('//tr/td[1]//text()').extract()
            symbol_1 = sel.xpath('//tr/td[2]//text()').extract()
            symbol_2 = sel.xpath('//tr//span[@class="market-native-price"]//text()').extract()
            symbol_3 = sel.xpath('//tr/td[3]//text()').extract()
            symbol_4 = sel.xpath('//tr/td[4]//text()').extract()
            symbol_5 = sel.xpath('//tr/td[5]//text()').extract()
            symbol_6 = sel.xpath('//tr/td[6]//text()').extract()
            print(text)
            #print((symbol_lower),(symbol_nodisplay),(symbol_power),(symbol_1),symbol_2,(symbol_3),(symbol_4),(symbol_5),(symbol_6))
            #a,b,c,d,e,f,g,h,j,k=LinkItem.item_type
            data = LinkItem()
            if len(symbol_lower) >0:
                data['symbol']= symbol_lower[0]
            if len(symbol_nodisplay) >0:
                data['symbol_nodisplay'] =symbol_nodisplay[0]
            if len(symbol_2) >0:
                data['symbol_price']  = re.search( r"(\d+\.?\d*)",symbol_1[0].replace(",","")).group()
            if len(symbol_3) >0:
                data['fudu'] = symbol_3[0]
            if len(symbol_4) >0:
                data['low'] = re.search( r"(\d+\.?\d*)",symbol_4[0].replace(",","")).group()
            if len(symbol_5) >0:
                data['high'] = re.search( r"(\d+\.?\d*)",symbol_5[0].replace(",","")).group()
            if len(symbol_6) >0:
                data['num'] = re.search( r"(\d+\.?\d*)",symbol_6[0].replace(",","")).group()
            match = re.search( r"_usdt",symbol_lower[0])
            if match:
                data['type'] ="usdt"
            match = re.search( r"_btc",symbol_lower[0])
            if match:
                data['type'] ="btc"
            match = re.search( r"_eth",symbol_lower[0])
            if match:
                 data['type'] ="eth"
            match = re.search( r"_okb",symbol_lower[0])
            if match:
                 data['type'] ="okb"
            yield data



        #print("@"*100,response.url)
        #print(data)


