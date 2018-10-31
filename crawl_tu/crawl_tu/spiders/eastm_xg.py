import scrapy
from crawl_tu.items import CrawlTuItem


class EastMoneySpider(scrapy.Spider):
    name = 'xg_yanbao'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'stock.eastmoney.com',
        'Referer': 'http://stock.eastmoney.com/report.html'
    }

    def start_requests(self):
        urls = []
        prefix = 'http://datainterface.eastmoney.com//EM_DataCenter/JS.aspx?type=NS&sty=NSSR&st=0&sr=-1'
        suffix = '&ps=50&js=var FvSrhgCJ={pages:(pc),data:[(x)]}&rt=51348978'
        for x in range(1, 2800):  # 2800
            p = str(x)
            urls.append('{0}{1}{2}{3}'.format(prefix, '&p=', p, suffix))
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = CrawlTuItem()
        data['content'] = response.body
        yield data
        # print(response.body)

