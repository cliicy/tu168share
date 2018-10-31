import scrapy
from crawl_tu.items import CrawlTuItem


class EastMoneySpider(scrapy.Spider):
    name = 'profit_forecast'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'stock.eastmoney.com',
        'Referer': 'http://stock.eastmoney.com/report.html'
    }

    def start_requests(self):
        urls = []
        prefix = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&' \
                 'cmd=C._A&sty=GEMCPF&st=(AllNum)&sr=-1'
        suffix = '&ps=50&cb=&js=var%20HcYkWPCP={"data":[(x)],"pages":"(pc)"}&' \
                 'token=3a965a43f705cf1d9ad7e1a3e429d622&rt=51351306'
        for x in range(1, 3600):  # 3600
            p = str(x)
            urls.append('{0}{1}{2}{3}'.format(prefix,  '&p=', p, suffix))
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = CrawlTuItem()
        data['content'] = response.body
        yield data
        # print(response.body)

