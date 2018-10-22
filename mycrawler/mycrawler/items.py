# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class AutohomeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = Field()

class LinkItem(Item):
    # define the fields for your item here like:
    # name = Field()
    coin = Field()
    symbol = Field()
    type = Field()
    symbol_nodisplay = Field()
    symbol_price = Field()
    fudu =  Field()
    high =  Field()
    low = Field()
    num = Field()

    url = Field()
    content = Field()
