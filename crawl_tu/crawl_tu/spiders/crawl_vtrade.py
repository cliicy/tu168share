import scrapy
# from scrapy import selector
# from crawl_tu.items import CrawlTuItem
from scrapy.selector import Selector


class EastMoneySpider(scrapy.Spider):
    name = 'vtrade'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'https://www.fcoin.com/ex',
        'Referer': 'https://exchange.fcoin.com/ex/main/btc/usdt'
    }

    def grab_fcoin_info(self,response):
        sym_list = []
        sel = response.xpath('//p[has-class("jss110 jss118 symbol")]')
        for p in sel:
            symbol = p.xpath("string(.)").extract()
            sym_list.append(symbol)
            # print(symbol)
            p1 = p.xpath('..')
            p2 = p1.xpath('..')[0]
            price = p2.xpath('.//p[@class="jss110 jss118 price"]/text()').extract()
            print('价格：', price)
            change = p2.xpath(
                './/span[@class="sc-fjdhpX AwYAJ" or @class="sc-fjdhpX fvAMlD"]//text()').extract()
            print('涨跌幅：', change)


    def grab_head(self, response):
        # news = {}
        list = response.xpath('//*[@class="news-cont"]//ul//li//div[@class="news-list"]').extract()
        for text in list:
            sel = Selector(text=text)
            link = sel.xpath('//dl//dt/a/@href').extract()
            title = sel.xpath('//dl//dt/a//text()').extract()
            zhaiyao = sel.xpath('//dl//dd//text()').extract()
            author = sel.xpath('//div[@class="time-author"]//text()').extract()
            time = sel.xpath('//div[@class="time"]//text()').extract()
            # print("#"*100)
            print(link, title, zhaiyao, author, time)

    def grap_stock_data(self, response):
        a_space = response.xpath('//div[@class="content tb14"]/table[@class="t1"]/thead[@class="h432"]/'
                                 'following-sibling::text()')
        # sa_space = a_space.xpath('/following-sibling::text()')  # //*[@id="dt_1"]/tbody/tr[1]/td[7]
        print('a_space', a_space)

    def grap_next_page(self, response):
        pass

    def start_requests(self):
        urls = ['https://exchange.fcoin.com/ex/main/btc/usdt']
        urls = ['F:\\Projects\\vTrade\\tcrawl\\mycrawler\\fcoin.html']
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        self.grab_fcoin_info(response)


if __name__ == '__main__':
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

