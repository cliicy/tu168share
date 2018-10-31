# coding=utf-8
# import subprocess
from multiprocessing import Process
from scrapy import cmdline


def do_crawl(spider):
    cmd = '{0} {1}'.format('scrapy crawl', spider)
    try:
        cmdline.execute(cmd.split())
    except Exception as e:
        print('发生错误=====', e)


def crawl_east_data():
    # 资金流
    # spider_list = ['today_hangye_money_flow']
    spider_list = ['today_hangye_money_flow', '5day_hangye_money_flow', '10day_hangye_money_flow',
                   'today_kailian_money_flow', '5days_kailian_money_flow', '10days_kailian_money_flow']
    for item in spider_list:
        pcrawl = Process(target=do_crawl, args=(item,))
        pcrawl.start()

    # 研报
    # spider_list = ['xg_yanbao']
    spider_list = ['gg_yanbao', 'xg_yanbao', 'hangye_yanbao', 'profit_forecast']
    for item in spider_list:
        pcrawl = Process(target=do_crawl, args=(item,))
        pcrawl.start()


if __name__ == '__main__':
    crawl_east_data()





