# -*- coding: utf-8 -*-
import scrapy
from baidu.items import BaiduItem
class Baidu(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ["dmoztools.net"]
    start_urls = [
       "http://fuliba.net"
    ]

    def parse(self, response):
        filename = response.url.split(".")[-1]+'.txt'
        for h2 in response.xpath('//article[@class="entry-common clearfix"]'):
            item = BaiduItem()
            item['title'] =  str.strip(h2.xpath('header/h2/a/text()').extract()[0])
            item['url'] = h2.xpath('header/h2/a/@href').extract()[0]
            # item['desc'] =str.strip(h2.xpath('header/div[2]/span/text()').extract()[0])
            yield item
