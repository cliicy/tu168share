import scrapy
from crawl_tu.pipelines import logo_coll


class HuobiSpider(scrapy.Spider):
    name = 'huobi'
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
        root = response.xpath('//div[@class="table-body"]')[0]
        # print(root)
        tab_data = root.xpath('.//div[@class="table-row pro-item up"]|.//div[@class="table-row pro-item down"]')
        for item in tab_data:
            ybdd = {}
            ybdd['exchange'] = 'huobi'
            index = item.xpath('.//div[@class="cell col-index"]//span[@class="index"]/text()').extract()[0].strip()
            ybdd['id'] = index
            icon_path = item.xpath('.//div[@class="cell col-icon"]//img/@src').extract()[0].strip()
            ybdd['logo'] = icon_path
            symbol = item.xpath('.//div[@class="cell col-1"]//h3/text()').extract()[0].strip()
            ybdd['sym'] = symbol
            money_flag = item.xpath('.//div[@class="cell col-2"]//span/text()').extract()[0].strip()
            price = item.xpath('.//div[@class="cell col-2"]/text()').extract()[0].strip()
            ybdd['Price'] = '{0}{1}'.format(money_flag, price)
            change = item.xpath('.//div[@class="cell col-3"]//span/text()').extract()[0].strip()
            ybdd['Change'] = change
            cap = item.xpath('.//div[@class="cell col-4"]/text()').extract()[0].strip()
            cap_flag = item.xpath('.//div[@class="cell col-4"]//span/text()').extract()[0].strip()
            ybdd['Cap'] = '{0}{1}'.format(cap_flag, cap)
            val = item.xpath('.//div[@class="cell col-5"]/text()').extract()[0].strip()
            ybdd['Val'] = val
            vol = item.xpath('.//div[@class="cell col-6"]/text()').extract()[0].strip()
            vol_flag = item.xpath('.//div[@class="cell col-6"]//span/text()').extract()[0].strip()
            ybdd['Volume'] = '{0}{1}'.format(vol_flag, vol)
            logo_coll.update({'sym': ybdd['sym'], 'exchange': ybdd['exchange']},
                             {'$set': {'sym': ybdd['sym'], 'Logo': ybdd['logo'], 'Price': ybdd['Price'],
                                       'Change': ybdd['Change'], 'Volume': ybdd['Volume'], 'Cap': ybdd['Cap'],
                                       'sym_id': ybdd['id'], 'exchange': ybdd['exchange'], 'api': 'crawl'}}, True)

    def start_requests(self):
        urls = ['https://www.huobiinfo.com/projects']
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

