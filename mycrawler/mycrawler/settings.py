# -*- coding: utf-8 -*-

# Scrapy settings for unionland project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mycrawler'

SPIDER_MODULES = ['mycrawler.spiders']
NEWSPIDER_MODULE = 'mycrawler.spiders'


DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.2)',
    'Accept': 'text/html',
    'Accept-Charset': 'utf-8;q=0.7,*;q=0.7',
    'Accept-Language': 'zh-cn,zh;q=0.5'
}
DNSCACHE_ENABLED = True
#REDIRECT_ENABLED = True
#LOG_LEVEL = 'WARNING'
DOWNLOAD_DELAY = 10
#RANDOMIZE_DOWNLOAD_DELAY = False
AJAXCRAWL_ENABLED = True
#REDIRECT_MAX_TIMES = 60
#REDIRECT_MAX_METAREFRESH_DELAY = 100
COOKIES_ENABLED = False
#COOKIES_DEBUG = True
DEFAULT_ITEM_CLASS = 'mycrawler.items.LinkItem'
#DEPTH_LIMIT = 1
CONCURRENT_REQUESTS = 20
REACTOR_THREADPOOL_MAXSIZE = 10
DNSCACHE_SIZE = 20000
CONCURRENT_REQUESTS_PER_DOMAIN = 10
CONCURRENT_ITEMS = 100
#USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
ITEM_PIPELINES = {
   #'mycrawler.pipelines.MySQLStoreSinaPipeline': 300,
   'mycrawler.pipelines.YanbaoPipeline': 300,
}
DOWNLOAD_HANDLERS = {
    'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    'phantomjs-http': 'mycrawler.downloader.handlers.phantomjs.PhantomJSDownloadHandler',
    'phantomjs-https': 'mycrawler.downloader.handlers.phantomjs.PhantomJSDownloadHandler'
}

SPIDER_MIDDLEWARES = {
    'mycrawler.middlewares.PhantomJSMiddleware': 10
}



DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'mycrawler.downloader_middlewares.RotateUserAgentMiddleware.RotateUserAgentMiddleware': 10
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'unionlandcrawler (+http://www.yourdomain.com)'


MYSQL_HOST = '192.168.1.108'
MYSQL_DBNAME = 'yuqing'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_CHARSET = "utf8"
#####
#MYSQL_HOST = '124.173.114.136'
#MYSQL_DBNAME = 'crawldb'
#MYSQL_USER = 'uland'
#MYSQL_PASSWD = 'uland^&82016'
