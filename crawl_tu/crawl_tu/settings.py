# -*- coding: utf-8 -*-

# Scrapy settings for crawl_tu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawl_tu'

SPIDER_MODULES = ['crawl_tu.spiders']
NEWSPIDER_MODULE = 'crawl_tu.spiders'

# HTTPERROR_ALLOWED_CODES = [400, 504]
HTTPERROR_ALLOWED_CODES = [400]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'crawl_tu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'crawl_tu.middlewares.CrawlTuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'crawl_tu.middlewares.CrawlTuDownloaderMiddleware': 543,
   # 'crawl_tu.middlewares.CrawlTuDownloaderMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'crawl_tu.pipelines.CrawlTuPipeline': 300,
   # 'crawl_tu.pipelines.TCrawlTuPipeline': 300,
}
emongodb = {
    "host": '172.24.132.208',
    "user": 'data',
    "password": 'data123',
    "db": 'invest',
    "port": '27017',
    "gg": 'east_fund_personal',  # 个股研报 document
    "hy": 'east_fund_hangye',  # 行业研报 document
    "xg": 'east_fund_xingu',  # 新股研报 document
    "pf": 'east_fund_profit_forecast',  # 个股盈利预测 document
    "tmf": 'today_hangye_money_flow',  # 今日行业资金流向 document
    "5mf": '5day_hangye_money_flow',  # 5日行业资金流向 document
    "10mf": '10day_hangye_money_flow',  # 10日行业资金流向 document
    "tkmf": 'today_kailian_money_flow',  # 今日概念板块资金流向 document
    "5tkmf": '5days_kailian_money_flow',  # 5日概念板块资金流向 document
    "10tkmf": '10days_kailian_money_flow',  # 10日概念板块资金流向 document
    "fcoin": 'fcoin',
    "marketP1": 'dw_market',
    "coin_logo": 'dw_coin_logo',
    "feixiaohao": 'dw_fxh',
    "rate": 'dw_currency_rate',
    "AI_News": 'jgy'
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
