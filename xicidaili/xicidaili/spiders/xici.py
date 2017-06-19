# -*- coding: utf-8 -*-
import scrapy
from xicidaili.items import XicidailiItem

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/53.0.2785.143 Safari/537.36'}
    def start_requests(self):
        urls = 'http://www.xicidaili.com/nn/1'
        yield scrapy.Request(url=urls, headers=self.headers, callback=self.parse)

    def parse(self, response):
        trlist = response.xpath('//tr[@class="odd"]')
        item = XicidailiItem()
        for tr in trlist:
            item['ip'] = tr.xpath('td[2]/text()').extract()[0]
            item['port'] = tr.xpath('td[3]/text()').extract()[0]
            item['type'] = tr.xpath('td[6]/text()').extract()[0]
            address = tr.xpath('td[4]/a/text()').extract()
            if address:
                item['address'] = address[0]
            else:
                item['address'] = '无地址'
            yield item
        for i in range(2, 5):
            url = 'http://www.xicidaili.com/nn/%d'%i
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)




