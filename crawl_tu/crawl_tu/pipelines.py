# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import crawl_tu.settings as st
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()
engine = create_engine(st.url)  # 创建引擎
DB_Session = sessionmaker(bind=engine)
session = DB_Session()


class CrawlTuPipeline(object):
    def process_item(self, item, spider):
        # print('内容===== '+item['context'])
        print('内容===== ')
        return item
