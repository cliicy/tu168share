# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawl_tu.settings import emongodb as mdb
import json
from pymongo import MongoClient
from datetime import datetime

mongo_url = 'mongodb://' + mdb["user"] + \
            ':' + mdb["password"] + '@' + mdb["host"] + ':' + \
            mdb["port"] + '/' + mdb["db"]
conn = MongoClient(mongo_url)
sdb = conn[mdb["db"]]


def changeWan2Yi(num):
    tnum = num * 0.0001
    if abs(tnum) >= 1:
        tnum = round(tnum, 2)
        return '{0}{1}'.format(tnum, '亿')
    else:
        num = round(num)
        return '{0}{1}'.format(num, '万')


class CrawlTuPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'gg_yanbao':
            p_coll = sdb[mdb["gg"]]
            ylist = ['2018预测-', '2019预测-', '2020预测-']
            plist = ['市盈率', '收益']
            '''
               2018预测市盈率	2019预测市盈率	 2020预测市盈率
             'syls': ['19.89',            '14.67',       '11.37', '', ''], 
            2018预测收益	2019预测收益	 2020预测收益
             'sys': ['0.66',			 '0.9', 		'1.16', '', ''], 
             '''
            # print('内容===== '+item['context'])
            body = item['content']
            try:
                body = (body.decode('utf-8')).replace("var YFTOUTEi=", "")
            except AttributeError as e:
                body = (body.decode('gbk')).replace("var YFTOUTEi=", "")
                print(e)
            # print('内容===== ', body)
            data = json.loads(body)
            # print('处理后的内容===== ', data)
            rdata = data['data']
            for item in rdata:
                # print(item)
                pos = 0
                for oy in ylist:
                    sr = oy + plist[0]
                    sp = oy + plist[1]
                    item[sr] = item['syls'][pos]
                    item[sp] = item['sys'][pos]
                    pos += 1
                item.pop('syls')
                item.pop('sys')
                p_coll.update({'datetime': item['datetime'], 'secuFullCode': item['secuFullCode']},
                              {'$set': item}, True)
        elif spider.name == 'xg_yanbao':
            xg_coll = sdb[mdb["xg"]]
            body = item['content']
            body = (body.decode('utf-8')).replace("var FvSrhgCJ=", "")
            if isinstance(body, str):
                # print('body 类型===== ', 'string')
                pages, rdata = body.split(',', 1)
                rdata = rdata[:-1]
                list_data = eval(rdata.split(':', 1)[1])
                print('获取到的数据：  ', list_data)
                for item in list_data:
                    ybdd = {}
                    dd = item.split(',')
                    ybdd['日期'] = dd[1]
                    ybdd['代码'] = dd[2]
                    ybdd['简称'] = dd[3]
                    ybdd['研报标题'] = dd[4]
                    ybdd['申购日期'] = dd[5]
                    ybdd['上市日期'] = dd[6]
                    ybdd['发行价'] = dd[7]
                    ybdd['发行市盈率'] = dd[8]
                    ybdd['最新价'] = dd[9]
                    ybdd['最新市盈率'] = dd[10]
                    ybdd['行业市盈率'] = dd[11]
                    ybdd['预测合理价格-下限'] = ''
                    ybdd['预测合理价格-上限'] = ''
                    ybdd['机构'] = dd[17]

                    xg_coll.update({'日期': ybdd['日期'], '代码': ybdd['代码'], '研报标题': ybdd['研报标题']},
                                   {'$set': ybdd}, True)
                # print('内容===== ', list_data)
            if isinstance(body, list):
                print('body 类型===== ', '列表')
            if isinstance(body, dict):
                print('body 类型===== ', '字典')
        elif spider.name == 'hangye_yanbao':
            hy_coll = sdb[mdb["hy"]]
            body = item['content']
            body = (body.decode('utf-8')).replace("var UopbhUvJ=", "")
            data = json.loads(body)
            # print('处理后行业研报的内容===== ', data)
            rdata = data['data']
            ybdd = {}
            for item in rdata:
                sdata = item.split(',')
                # print('---', item)
                # print('---', sdata)
                ybdd['报告日期'] = sdata[1]
                ybdd['行业名称'] = sdata[10]
                ybdd['涨跌幅'] = sdata[11]
                # ybdd['相关'] = item[1]
                ybdd['标题'] = sdata[9]
                ybdd['评级类别'] = sdata[6]
                ybdd['评级变动'] = sdata[0]
                ybdd['机构名称'] = sdata[4]
            hy_coll.update({'报告日期': ybdd['报告日期'], '行业名称': ybdd['行业名称'], '标题': ybdd['标题']},
                           {'$set': ybdd}, True)
        elif spider.name == 'profit_forecast':
                ylist = ['2018预测-', '2019预测-', '2020预测-']
                plist = ['收益', '市盈率']
                pf_coll = sdb[mdb["pf"]]
                body = item['content']
                # print('内容===== ', body)
                body = (body.decode('utf-8')).replace("var HcYkWPCP=", "")
                # print('内容去杂后===== ', body)
                if isinstance(body, list):
                    print('body 类型===== ', '列表')
                if isinstance(body, dict):
                    print('body 类型===== ', '字典')
                if isinstance(body, str):
                    print('body 类型===== ', '字符串')
                data = json.loads(body)['data']
                print('实体数据===== ', data)
                for item in data:
                    ybdd = {}
                    sdata = item.split(',')
                    ybdd['代码'] = sdata[1]
                    ybdd['名称'] = sdata[2]
                    ybdd['最新价'] = sdata[3]
                    ybdd['涨跌幅'] = sdata[4]
                    ybdd['研报数'] = sdata[5]
                    ybdd['机构投资评级(近六个月)-买入'] = sdata[6]
                    ybdd['机构投资评级(近六个月)-增持'] = sdata[7]
                    ybdd['机构投资评级(近六个月)-中性'] = sdata[8]
                    ybdd['机构投资评级(近六个月)-减持'] = sdata[9]
                    ybdd['机构投资评级(近六个月)-卖出'] = sdata[10]
                    ybdd['2017实际-收益'] = sdata[11]
                    pos = 12  # 2017实际-收益 后面的值就是预测数据
                    for oy in ylist:
                        sr = oy + plist[0]
                        sp = oy + plist[1]
                        ybdd[sr] = sdata[pos]
                        ybdd[sp] = sdata[pos+1]
                        pos += 2
                    pf_coll.update({'代码': ybdd['代码'], '名称': ybdd['名称']}, {'$set': ybdd}, True)
        elif spider.name == 'today_hangye_money_flow':
            body = item['content']
            body = (body.decode('utf-8')).replace("var AKACTekX=", "")
            print('内容===== ', body)
            if isinstance(body, list):
                print('body 类型===== ', '列表')
            if isinstance(body, dict):
                print('body 类型===== ', '字典')
            if isinstance(body, str):
                print('body 类型===== ', '字符串')
                pages, rdata = body.split(',', 1)
                rdata = rdata[:-1]
                list_data = eval(rdata.split(':', 1)[1])
                print('获取到的数据：  ', list_data)
                for item in list_data:
                    ybdd = {}
                    sdata = item.split(',')
                    ybdd['名称'] = sdata[2]
                    ybdd['今日涨跌幅'] = sdata[3]+'%'
                    ybdd['今日主力净流入-净额'] = changeWan2Yi(float(sdata[4]))
                    ybdd['今日主力净流入-净占比'] = sdata[5]+'%'

                    ybdd['今日超大单净流入-净额'] = changeWan2Yi(float(sdata[6]))
                    ybdd['今日超大单净流入-净占比'] = sdata[7]+'%'

                    ybdd['今日大单净流入-净额'] = changeWan2Yi(float(sdata[8]))
                    ybdd['今日大单净流入-净占比'] = sdata[9]+'%'

                    ybdd['今日中单净流入-净额'] = changeWan2Yi(float(sdata[10]))
                    ybdd['今日中单净流入-净占比'] = sdata[11]+'%'

                    ybdd['今日小单净流入-净额'] = changeWan2Yi(float(sdata[12]))
                    ybdd['今日小单净流入-净占比'] = sdata[13]+'%'

                    ybdd['今日主力净流入-最大股'] = sdata[14]
                    tmf_coll = sdb[mdb["tmf"]]
                    tmf_coll.update({'名称': ybdd['名称']}, {'$set': ybdd}, True)
        elif spider.name == '5day_hangye_money_flow':
            body = item['content']
            body = (body.decode('utf-8')).replace("var zWpcawma=", "")
            print('内容===== ', body)
            if isinstance(body, list):
                print('body 类型===== ', '列表')
            if isinstance(body, dict):
                print('body 类型===== ', '字典')
            if isinstance(body, str):
                print('body 类型===== ', '字符串')
                pages, rdata = body.split(',', 1)
                rdata = rdata[:-1]
                list_data = eval(rdata.split(':', 1)[1])
                print('获取到的数据：  ', list_data)
                for item in list_data:
                    ybdd = {}
                    sdata = item.split(',')
                    ybdd['名称'] = sdata[2]
                    ybdd['5日涨跌幅'] = sdata[3]+'%'
                    ybdd['5日主力净流入-净额'] = changeWan2Yi(float(sdata[4]))
                    ybdd['5日主力净流入-净占比'] = sdata[5]+'%'

                    ybdd['5日超大单净流入-净额'] = changeWan2Yi(float(sdata[6]))
                    ybdd['5日超大单净流入-净占比'] = sdata[7]+'%'

                    ybdd['5日大单净流入-净额'] = changeWan2Yi(float(sdata[8]))
                    ybdd['5日大单净流入-净占比'] = sdata[9]+'%'

                    ybdd['5日中单净流入-净额'] = changeWan2Yi(float(sdata[10]))
                    ybdd['5日中单净流入-净占比'] = sdata[11]+'%'

                    ybdd['5日小单净流入-净额'] = changeWan2Yi(float(sdata[12]))
                    ybdd['5日小单净流入-净占比'] = sdata[13]+'%'

                    ybdd['5日主力净流入-最大股'] = sdata[14]
                    mf5_coll = sdb[mdb["5mf"]]
                    mf5_coll.update({'名称': ybdd['名称']}, {'$set': ybdd}, True)
        elif spider.name == '10day_hangye_money_flow':
            body = item['content']
            body = (body.decode('utf-8')).replace("var NmXFNoAK=", "")
            print('内容===== ', body)
            if isinstance(body, list):
                print('body 类型===== ', '列表')
            if isinstance(body, dict):
                print('body 类型===== ', '字典')
            if isinstance(body, str):
                print('body 类型===== ', '字符串')
                pages, rdata = body.split(',', 1)
                rdata = rdata[:-1]
                list_data = eval(rdata.split(':', 1)[1])
                print('获取到的数据：  ', list_data)
                for item in list_data:
                    ybdd = {}
                    sdata = item.split(',')
                    ybdd['名称'] = sdata[2]
                    ybdd['10日涨跌幅'] = sdata[3]+'%'
                    ybdd['10日主力净流入-净额'] = changeWan2Yi(float(sdata[4]))
                    ybdd['10日主力净流入-净占比'] = sdata[5]+'%'

                    ybdd['10日超大单净流入-净额'] = changeWan2Yi(float(sdata[6]))
                    ybdd['10日超大单净流入-净占比'] = sdata[7]+'%'

                    ybdd['10日大单净流入-净额'] = changeWan2Yi(float(sdata[8]))
                    ybdd['10日大单净流入-净占比'] = sdata[9]+'%'

                    ybdd['10日中单净流入-净额'] = changeWan2Yi(float(sdata[10]))
                    ybdd['10日中单净流入-净占比'] = sdata[11]+'%'

                    ybdd['10日小单净流入-净额'] = changeWan2Yi(float(sdata[12]))
                    ybdd['10日小单净流入-净占比'] = sdata[13]+'%'

                    ybdd['10日主力净流入-最大股'] = sdata[14]
                    mf10_coll = sdb[mdb["10mf"]]
                    mf10_coll.update({'名称': ybdd['名称']}, {'$set': ybdd}, True)
        elif spider.name == 'today_kailian_money_flow':
            body = item['content']
            body = (body.decode('utf-8')).replace("var OSLDjtXS=", "")
            print('内容===== ', body)
            if isinstance(body, list):
                print('body 类型===== ', '列表')
            if isinstance(body, dict):
                print('body 类型===== ', '字典')
            if isinstance(body, str):
                print('body 类型===== ', '字符串')
                pages, rdata = body.split(',', 1)
                rdata = rdata[:-1]
                list_data = eval(rdata.split(':', 1)[1])
                print('获取到的数据：  ', list_data)
                for item in list_data:
                    ybdd = {}
                    sdata = item.split(',')
                    ybdd['名称'] = sdata[2]
                    ybdd['今日涨跌幅'] = sdata[3]+'%'
                    ybdd['今日主力净流入-净额'] = changeWan2Yi(float(sdata[4]))
                    ybdd['今日主力净流入-净占比'] = sdata[5]+'%'

                    ybdd['今日超大单净流入-净额'] = changeWan2Yi(float(sdata[6]))
                    ybdd['今日超大单净流入-净占比'] = sdata[7]+'%'

                    ybdd['今日大单净流入-净额'] = changeWan2Yi(float(sdata[8]))
                    ybdd['今日大单净流入-净占比'] = sdata[9]+'%'

                    ybdd['今日中单净流入-净额'] = changeWan2Yi(float(sdata[10]))
                    ybdd['今日中单净流入-净占比'] = sdata[11]+'%'

                    ybdd['今日小单净流入-净额'] = changeWan2Yi(float(sdata[12]))
                    ybdd['今日小单净流入-净占比'] = sdata[13]+'%'

                    ybdd['今日主力净流入-最大股'] = sdata[14]
                    tkmf_coll = sdb[mdb["tkmf"]]
                    tkmf_coll.update({'名称': ybdd['名称']}, {'$set': ybdd}, True)
        elif spider.name == '5days_kailian_money_flow':
            body = item['content']
            body = (body.decode('utf-8')).replace("var kKrfEPzl=", "")
            # print('内容===== ', body)
            if isinstance(body, list):
                print('body 类型===== ', '列表')
            if isinstance(body, dict):
                print('body 类型===== ', '字典')
            if isinstance(body, str):
                print('body 类型===== ', '字符串')
                pages, rdata = body.split(',', 1)
                rdata = rdata[:-1]
                list_data = eval(rdata.split(':', 1)[1])
                print('获取到的数据：  ', list_data)
                for item in list_data:
                    ybdd = {}
                    sdata = item.split(',')
                    ybdd['名称'] = sdata[2]
                    ybdd['5日涨跌幅'] = sdata[3]+'%'
                    ybdd['5日主力净流入-净额'] = changeWan2Yi(float(sdata[4]))
                    ybdd['5日主力净流入-净占比'] = sdata[5]+'%'

                    ybdd['5日超大单净流入-净额'] = changeWan2Yi(float(sdata[6]))
                    ybdd['5日超大单净流入-净占比'] = sdata[7]+'%'

                    ybdd['5日大单净流入-净额'] = changeWan2Yi(float(sdata[8]))
                    ybdd['5日大单净流入-净占比'] = sdata[9]+'%'

                    ybdd['5日中单净流入-净额'] = changeWan2Yi(float(sdata[10]))
                    ybdd['5日中单净流入-净占比'] = sdata[11]+'%'

                    ybdd['5日小单净流入-净额'] = changeWan2Yi(float(sdata[12]))
                    ybdd['5日小单净流入-净占比'] = sdata[13]+'%'

                    ybdd['5日主力净流入-最大股'] = sdata[14]
                    tkmf5_coll = sdb[mdb["5tkmf"]]
                    tkmf5_coll.update({'名称': ybdd['名称']}, {'$set': ybdd}, True)
        elif spider.name == '10days_kailian_money_flow':
            body = item['content']
            body = (body.decode('utf-8')).replace("var jMgwlSkv=", "")
            # print('内容===== ', body)
            if isinstance(body, list):
                print('body 类型===== ', '列表')
            if isinstance(body, dict):
                print('body 类型===== ', '字典')
            if isinstance(body, str):
                print('body 类型===== ', '字符串')
                pages, rdata = body.split(',', 1)
                rdata = rdata[:-1]
                list_data = eval(rdata.split(':', 1)[1])
                print('获取到的数据：  ', list_data)
                for item in list_data:
                    ybdd = {}
                    sdata = item.split(',')
                    ybdd['名称'] = sdata[2]
                    ybdd['10日涨跌幅'] = sdata[3]+'%'
                    ybdd['10日主力净流入-净额'] = changeWan2Yi(float(sdata[4]))
                    ybdd['10日主力净流入-净占比'] = sdata[5]+'%'

                    ybdd['10日超大单净流入-净额'] = changeWan2Yi(float(sdata[6]))
                    ybdd['10日超大单净流入-净占比'] = sdata[7]+'%'

                    ybdd['10日大单净流入-净额'] = changeWan2Yi(float(sdata[8]))
                    ybdd['10日大单净流入-净占比'] = sdata[9]+'%'

                    ybdd['10日中单净流入-净额'] = changeWan2Yi(float(sdata[10]))
                    ybdd['10日中单净流入-净占比'] = sdata[11]+'%'

                    ybdd['10日小单净流入-净额'] = changeWan2Yi(float(sdata[12]))
                    ybdd['10日小单净流入-净占比'] = sdata[13]+'%'

                    ybdd['10日主力净流入-最大股'] = sdata[14]
                    tkmf10_coll = sdb[mdb["10tkmf"]]
                    tkmf10_coll.update({'名称': ybdd['名称']}, {'$set': ybdd}, True)
        elif spider.name == 'fcoin_spider':
            ybdd = {}
            vChange = item['vChange']
            ybdd['Change'] = vChange + '%'
            dfcoin_coll = sdb[mdb["fcoin"]]
            dfcoin_coll.update({'Change': ybdd['Change']}, {'$set': ybdd}, True)
        return item


class TCrawlTuPipeline(object):
    def process_item(self, item, spider):
        # head = item['head']
        end = datetime.now()
        spend = end - item['start_t']
        print('消耗时间: ', spend)
        return item


if __name__ == '__main__':
    # body = '{pages:55,data:["AP201810251221240617,2018/10/25","AP201810241220091942,2018/10/24"]}'
    # if isinstance(body, str):
    #     print('body 类型===== ', 'string')
    #     page, rd = body.split(',', 1)
    #     print('内容11=== ', rd)
    #     rd = rd[:-1]
    #     print('内容===== ', rd)
    #     list_data = rd.split(':', 1)[1]
    #     print('data内容===== ', list_data)
    #     for item in eval(list_data):
    #         print(item)
    # if isinstance(body, list):
    #     print('body 类型===== ', '列表')
    # if isinstance(body, dict):
    #     print('body 类型===== ', '字典')
    sdata = '-12774'
    # sdata = '12774'
    # sdata = '30277'
    # sdata = '1954'
    # sdata = '138307.98'
    rr = changeWan2Yi(float(sdata))
    print(rr)
    pass
    # xg_coll = sdb[mdb["xg"]]
    # ybdd = {}
    # ybdd['日期'] = '2018/9/28 0:00:00'
    # ybdd['代码'] = '002940'
    # ybdd['简称'] = '000'
    # ybdd['研报标题'] = '昂利康新股网下询价策略'
    # match = {"$match": {"日期": ybdd['日期'], "代码": ybdd['代码'], "简称": ybdd['简称'], "研报标题": ybdd['研报标题']}}
    # sort = {"$sort": {"日期": -1}}
    # pipeLine = [match, sort]
    # xg_coll.aggregate(pipeLine)
    # xg_coll.insert(ybdd)
    # xg_coll.update({'简称': ybdd['简称']}, {'$set': ybdd}, True)
    # print('aa')
