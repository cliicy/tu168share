# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field


class CrawlTuItem(Item):
    # define the fields for your item here like:
    xg = Field()
    # pass
    # head = Field()
    news = Field()
    content = Field()
    vChange = Field  # 涨跌幅
    # data = Field()
    # code = Field()
    # name = Field()
    # relevance = Field()
    # res_report = Field()
    # esclate = Field()
    # esc_change = Field()
    # org_change = Field()
    # profit = Field()
    # forecast2018 = Field()
    # Forecast2019 = Field()
    # low = Field()
    # num = Field()
    # url = Field()

    site_name = Field()
    url = Field()

