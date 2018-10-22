import scrapy
from crawl_tu.items import CrawlTuItem


class EastMoneySpider(scrapy.Spider):
    name = 'esstock_spider'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'data.eastmoney.com',
        'Referer': 'http://data.eastmoney.com/report/'
    }

    def start_requests(self):
        urls = []
        prefix1 = 'http://data.eastmoney.com/report/'
        # prefix1 = 'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0x'
        # for x in range(1, 200):
        #     p = str(x)
        #     urls.append('{0}{1}'.format(prefix, 'ps=50&p=''"+p+"&mkt=0&stat=0&cmd=4&code=&rt=51330470'))
        urls.append(prefix1)
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        item = CrawlTuItem()
        # a_space = response.xpath('//div[@class="tit"]')
        a_space = response.xpath('//table[@class="t1"]/*/tbody/tr/')
        # a_space = response.xpath('//div[@class="content tb14"]/*/tr/th[1]')
        # print('response.url='+response.url)
        for a in a_space:
            print('测试---', a.xpath('text()').extract())
            # item['content'] = a.xpath('text()').extract()

        # yield item


# if __name__ == '__main__':
#     url = 'http://stock.eastmoney.com/report.html'
#     filename = url.split('/')[-1]
#     print(filename)
#     # filename = url.split('/')[-1]
#     for x in range(0, 200):
#         p = str(x)
#         y = x+1
#         print('aa')
