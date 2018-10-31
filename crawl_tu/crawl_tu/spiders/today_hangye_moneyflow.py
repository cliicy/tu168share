import scrapy
from crawl_tu.items import CrawlTuItem


class EastMoneySpider(scrapy.Spider):
    name = 'today_hangye_money_flow'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'stock.eastmoney.com',
        'Referer': 'http://stock.eastmoney.com/report.html'
    }

    def start_requests(self):
        urls = []
        prefix = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cmd=C._BKHY&type=ct&' \
                 'st=(BalFlowMain)&sr=-1'
        suffix = '&ps=50&js=var%20AKACTekX={pages:(pc),data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&' \
                 'sty=DCFFITABK&rt=51362315'
        for x in range(1, 3):  #
            p = str(x)
            urls.append('{0}{1}{2}{3}'.format(prefix,  '&p=', p, suffix))
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = CrawlTuItem()
        data['content'] = response.body
        yield data
        # print(response.body)

