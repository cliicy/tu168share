import scrapy
from crawl_tu.items import CrawlTuItem


class EastMoneySpider(scrapy.Spider):
    name = 'tt_stock_spider'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'stock.eastmoney.com',
        'Referer': 'http://stock.eastmoney.com/report.html'
    }

    def start_requests(self):
        urls = ['http://data.eastmoney.com/report/']
        # urls = ['http://data.eastmoney.com/report/',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0y',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0z',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT00',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT01',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT02',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT03',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT04',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT05',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMA==',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMQ==',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMg==',
        #         'http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0xMw==']
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = CrawlTuItem()
        # data['url'] = response.url
        data['content'] = response.body
        # yield data
        print(response.body)
