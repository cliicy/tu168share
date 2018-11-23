import scrapy
from crawl_tu.pipelines import fxh_coll


class HuobiSpider(scrapy.Spider):
    name = 'exchange_list'
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
        ex_dir = response.xpath('//table[@class="table exchange-table"]//tr')
        # print(ex_dir)
        for item in ex_dir:
            ybdd = {}
            sel_td = item.xpath('.//td[1]')
            id = sel_td.xpath('./text()').extract()
            if len(id):
                # print('id= ', id)
                ybdd['id'] = id[0]
                img = item.xpath('.//td[2]/a//img/@src').extract()
                # print('img= ', img)
                ybdd['logo'] = img[0]
                name = item.xpath('.//td[2]//text()').extract()
                # print('name= ', name)
                ybdd['exchange'] = name[1].lstrip().rstrip()
                h24_vol = item.xpath('.//td[3]//text()').extract()
                # print('24h volume= ', h24_vol)
                ybdd['volume'] = h24_vol[0]
                sym_num = item.xpath('.//td[4]//text()').extract()
                # print('交易对总个数：', sym_num)
                ybdd['total_sym'] = sym_num[0]
                location = item.xpath('.//td[5]//text()').extract()
                # print('location：', location)
                ybdd['location'] = location[0]
                fxh_coll.update({'id': ybdd['id'], 'exchange': ybdd['exchange'], 'volume': ybdd['volume'],
                                 'location': ybdd['location'], 'total_sym': ybdd['total_sym']},
                                {'$set': {'id': ybdd['id'], 'Logo': ybdd['logo'], 'exchange': ybdd['exchange'],
                                          'volume': ybdd['volume'], 'total_sym': ybdd['total_sym'],
                                          'location': ybdd['location'], 'api': 'crawl'}}, True)

    def start_requests(self):
        urls = ['https://www.feixiaohao.com/exchange/?mineable=1']
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

