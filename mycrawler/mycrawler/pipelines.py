# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
import codecs
import re
import time
from datetime import datetime
import string
import csv
import os
import json


class YanbaoPipeline(object):
    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = os.path.dirname(__file__) + '\\data\\yanbao.csv'
        # store_file = "d://dieshi_result/ok_hangqing.csv"
        # 打开(创建)文件
        self.file = open(store_file,'w')
        # csv写法
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        # page = re.match('.*&p=(.*)&mkt=.*', item['url']).group(1)

        body = item['content']
        try:
            body = (body.decode('utf-8')).replace("var eNyUNdeY=","")
        except:
            body = (body.decode('gbk')).replace("var eNyUNdeY=","")
        # dict=json.loads(body)
        # list =dict['data']
        print('哈哈', body)
        # print("#"*100)
        # print(type(dict),page,len(list))
        # for x in list:
        #     if x is None:
        #         continue
        #     a=x['datetime']
        #     b=x['secuFullCode']
        #     c=x['secuName']
        #     d=x['title']
        #     e=x['change']
        #     f=x['insName']
        #     g=x['sys'][0]
        #     h=x['syls'][0]
        #     i=x['sys'][1]
        #     j=x['syls'][1]
        #     meta =[a,b,c,d,e,f,g,h,i,j]
        #     self.writer.writerow(meta)




