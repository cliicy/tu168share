import scrapy
from crawl_tu.items import CrawlTuItem


class EastMoneySpider(scrapy.Spider):
    name = 'hangye_yanbao'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'stock.eastmoney.com',
        'Referer': 'http://stock.eastmoney.com/report.html'
    }

    def start_requests(self):
        urls = []
        prefix1 = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HYSR&mkt=0&stat=0&'
        prefix2 = 'cmd=4&code=&sc=&ps=50'
        suffix = '&js=var%20UopbhUvJ={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count' \
                 ' %22:%22(count)%22}&rt=51348585'
        for x in range(1, 76350):  #
            p = str(x)
            urls.append('{0}{1}{2}{3}{4}'.format(prefix1, prefix2, '&p=', p, suffix))
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = CrawlTuItem()
        data['content'] = response.body
        yield data
        # print(response.body)

