# -*- coding: utf-8 -*-
import scrapy
from douban_movie.items import DoubanMovieItem


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headers)




    def parse(self, response):
        item = DoubanMovieItem()
        divlist = response.xpath(r"//div[@class='pic']")
        for div in divlist:
            item['Url'] = div.xpath("a/@href").extract_first()
            item['Img_url'] = div.xpath('a/img/@src').extract_first()
            yield item
            yield scrapy.Request(url=item['Url'], meta={'item':item} , callback=self.parse_movie)
        next_href = response.xpath('//link[@rel="next"]/@href').extract()
        if next_href:
            nexturl = 'http://movie.douban.com/top250'+ next_href[0]
            yield scrapy.Request(url=nexturl, headers=self.headers)




    def parse_movie(self, response):
        item = response.meta['item']
        item['title'] = response.xpath('//span[@property="v:itemreviewed"/text()').extract()
        item['vote'] = response.xpath('//span[@property="v:votes"/text()').extract()
        item['replay'] = response.xpath('//*[@id="hot-comments"]/div[1]/div/p/text()').extract()
        yield item
