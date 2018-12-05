import scrapy
from crawl_tu.pipelines import rate_coll
import json


class HuobiSpider(scrapy.Spider):
    name = 'huobi_rate_data'
    # headers = {
    #     'User_Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    #                   'AppleWebKit/537.36 (KHTML, like Gecko)'
    #                   'Chrome/70.0.3538.102 Safari/537.36',
    #     'Host': 'https://www.huobiinfo.com',
    #     'Referer': 'https://www.huobiinfo.com'
    # }
    headers = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3)'
                      ' AppleWebKit/536.5 (KHTML, like Gecko)'
                      'Chrome/19.0.1084.54 Safari/536.5'
    }

    def grab_data(self, response):
        body = response.xpath('//body').extract()[0]
        body = body.replace('<body><p>', '')
        body = body.replace('</p></body>', '')
        print(type(body))
        dd = json.loads(body)
        print(dd)
        for item in dd['data']:
            ybdd = {}
            ybdd['exchange'] = 'huobi'
            name = item['name']
            if name == 'usd_cny' or name == 'btc_cny' or name == 'usdt_cny':
                ybdd['sym'] = item['name']
                rate_coll.update({'sym': ybdd['sym'], 'exchange': ybdd['exchange']},
                                 {'$set': {'sym': ybdd['sym'], 'rate': item['rate'],  'api': 'crawl'}}, True)

    def start_requests(self):
        urls = ['https://www.huobi.co/-/x/general/exchange_rate/list?r=4fxk3z101nj']
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        self.grab_data(response)


if __name__ == '__main__':
    # grab_head()
    # pass
    # start = timeit.default_timer()
    # print('aaaa')
    # end = timeit.default_timer()
    # print(str(end - start))
    # start = datetime.now()
    # for i in range(10):
    #     print('aaa')
    # end = datetime.now()
    # spend = end - start
    # print('消耗时间: ', spend)

    # start = time.clock()
    # print('aaa')
    # elapsed = (time.clock() - start)
    # print("Time used:", elapsed)
    pass
    # url = 'http://stock.eastmoney.com/report.html'
    # filename = url.split('/')[-1]
    # print(filename)
    # # filename = url.split('/')[-1]
    # for x in range(0, 200):
    #     p = str(x)
    #     y = x+1
    #     print('aa')

