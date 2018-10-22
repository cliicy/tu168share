# -*- coding: utf-8 -*-
from scrapy.http import Headers, HtmlResponse
from scrapy.utils.decorator import inthread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys

class PhantomJSDownloadHandler(object):
    def __init__(self, settings):
        pass

    @inthread
    def download_request(self, request, spider):
        # args = ['--ignore-ssl-errors=true', '--load-images=false']
        # Remove 'phantomjs-' prefix
        print("#"*100,request.url)
        url = request.url[10:]
        #print(type(url))
        # driver = webdriver.PhantomJS(service_args=args,
        #     executable_path=\
        #     'E:/learn/software/phantomjs-2.0.0-windows/bin/phantomjs',
        #     port=65000)
        # driver = webdriver.PhantomJS(executable_path=\
        #     'E:/learn/software/phantomjs-2.0.0-windows/bin/phantomjs')  #windows
        driver = webdriver.PhantomJS()   #centos
        #driver = webdriver.Firefox()  #centos
        # driver = webdriver.Chrome(executable_path="C:/Users/LENOVO/Desktop/to/chromedriver.exe")

        # time.sleep(20)  #dyh did it
        #WebDriverWait(driver, 30)
        driver.get(url)
        #print()
        time.sleep(30)
        #body = driver.find_element_by_xpath('//html').get_attribute("outerHTML") #dyh did it
        body = driver.find_element_by_xpath('//*').get_attribute("outerHTML")
        #headers = driver.find_element_by_xpath('//head').get_attribute("innerHTML")
        #headers,不确定编码时，从headers里取charset值
        driver.quit()
        # Set header so httpcache chooses the appropriate Response class
        #headers = Headers({'Content-Type': 'text/html'})
        headers = Headers({'Accept-Charset': 'utf-8;q=0.7,*;q=0.7', 'Accept-Language': 'zh-cn,zh;q=0.5','User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'})
        #print body
        body = body.encode("utf-8")
        #url = url.encode("utf-8")
        #print(body)
        return HtmlResponse(url=url, headers=headers, body=body)
