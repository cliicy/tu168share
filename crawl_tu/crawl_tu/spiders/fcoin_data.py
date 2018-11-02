import scrapy
from crawl_tu.items import CrawlTuItem
import re


class FcoinSpider(scrapy.Spider):
    name = 'fcoin_spider'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'https://www.fcoin.com/',
        'Referer': 'https://exchange.fcoin.com/ex/main/btc-usdt/'
    }

    def grab_head(self, response):
        a_space = response.xpath('//div[@class="jss110 jss118 jss136 jss133 jss370"]')
        # change = re.findall(r'<div class="coinprice">(.*?)<span', coin_price[0], re.S)

        # head = []
        # n = 2
        # pos = 0
        for a in a_space:
            ss = a.xpath('string(.)').extract()[0]
            # head.append(ss)
            print('测试---', ss)
        return ss

    def grap_stock_data(self, response):
        a_space = response.xpath('//div[@class="content tb14"]/table[@class="t1"]/thead[@class="h432"]/'
                                 'following-sibling::tbody')
        sa_space = a_space.xpath('/following-sibling::text()')  # //*[@id="dt_1"]/tbody/tr[1]/td[7]
        print(a_space)
        print(sa_space)
        # a_each = a_space.xpath('//*')
        # print(a_each)
        # for each in a_space:
        #     print(each)
            # print(each.extract())
        #     a_each = each.xpath('/tr[@class=""]/td')
        #     print(a_each)
        #     ss = each.xpath('string(.)').extract()
            # ss = each.xpath('string(.)').extract()
            # print(ss)
            # ss = "".join(ss.split())
            # print('数据：', ss)
        # for a in a_space:
        #         #     ss = a.xpath('string(.)').extract()[0]
        #         #     print('获取股市数据---', ss)

    def grap_next_page(self, response):
        a_space = response.xpath('//div[@class="Page"][@id="PageCont"]/following-sibling/span[@class="at"]')
                                 # '/following-sibling::a[text()=="下一页"]')
        print(a_space)
        for a in a_space:
            print(a)
        pass

    def start_requests(self):
        # urls = ['www.baidu.com']
        urls = ['https://exchange.fcoin.com/ex/main/btc/usdt']
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        item = CrawlTuItem()
        item['vChange'] = self.grab_head(response)
        # self.grap_stock_data(response)
        # self.grap_next_page(response)
        yield item


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

