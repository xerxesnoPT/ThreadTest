# -*- coding: utf-8 -*-
import scrapy


class Zhihu1Spider(scrapy.Spider):
    name = "zhihu1"
    allowed_domains = ["www.zhihu.com"]
    user_url = 'https://www.zhihu.com/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    def start_requests(self):
        yield scrapy.Request(url = self.user_url,headers=self.headers, callback=self.parse_follows)

    def parse_follows(self,response):
        print(response.body)
