import scrapy
from crawl_tu.items import CrawlTuItem
from scrapy.selector import Selector
import timeit
from datetime import datetime
ylist = ['2018预测', '2019预测']


class EastMoneySpider(scrapy.Spider):
    name = 'test_spider'
    headers = {
        'User_Agent': 'User-Agent:Mozilla/5.0 (X11;Linux x86_64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'stock.eastmoney.com',
        'Referer': 'http://stock.eastmoney.com/report.html'
        # 'Host': 'http://www.sogou321.com/',
        # 'Referer': 'http://www.sogou321.com/'

    }

    def grab_head(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="sortSite"]/li/em')
        items = []
        for site in sites:
            item = CrawlTuItem()
            url_local = site.xpath('a/@href').extract()
            site_name_local = site.xpath('a/text()').extract()
            item['url'] = [u.encode('utf-8') for u in url_local]
            item['site_name'] = [site_name_local]  # s.encode('utf-8') for s in site_name_local
            items.append(item)
        print(items)
        return items
        #
        # news = {}
        # sel = Selector(response)
        # sites = sel.xpath('//div[@class="stock"]')
        # print(sites)
        # items = []
        # for site in sites:
        #     link = site.xpath('a/@href').extract()
        #     news['auth'] = 'luo'
        #     news['link'] = link
        #     news['title'] = 'hello'
        #     news['time'] = '2018-11-02'
        # return news
        # pass
        # a_space = response.xpath('.//ul/li')
        # # a_space = response.xpath('//div[@id="NewsList1_UpdatePanel1"]//li/text()')
        #
        # print(a_space)
        # # sa_space = response.xpath('//div[@class="content tb14"]/table[@class="t1"]/thead[@class="h432"]/tr[2]'
        # #                           '/th[position()<5]')
        # news = []
        # # n = 2
        # # pos = 0
        # for a in a_space:
        #     ss = a.xpath('string(.)').extract()
        # #     head.append(ss)
        #     print('测试---', ss)
        # # for sa in sa_space:
        # #     ss = sa.xpath('string(.)').extract()[0]
        # #     ss = "".join(ss.split())
        # #     head.append('{0}-{1}'.format(ylist[n % 2], ss))
        # #     pos += 1
        # #     if pos > 1:
        # #         n += 1
        # #     print('测试 子预测栏目---', ss)
        # #
        # return news

    def grap_stock_data(self, response):
        a_space = response.xpath('//div[@class="content tb14"]/table[@class="t1"]/thead[@class="h432"]/'
                                 'following-sibling::text()')
        # sa_space = a_space.xpath('/following-sibling::text()')  # //*[@id="dt_1"]/tbody/tr[1]/td[7]
        print('a_space', a_space)
        # print(sa_space)
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
        urls = ['http://stock.eastmoney.com/report.html']
        # urls = ['http://stock.eastmoney.com/report.html']
        # urls = ['http://jgy.com/']
        # urls = ['http://www.sogou321.com/']
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="report_search"]/li')
        print(sites)
        items = []
        for site in sites:
            item = CrawlTuItem()
            url_local = site.xpath('div[@class="n1"]/text()').extract()
            print(url_local)
            # site_name_local = site.xpath('a/text()').extract()
            # item['url'] = [u.encode('utf-8') for u in url_local]
            # item['site_name'] = [site_name_local]  # s.encode('utf-8') for s in site_name_local
            items.append(item)

        return items
        # return self.grab_head(response)
        # self.grap_stock_data(response)
        # self.grap_next_page(response)
        # yield item


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

