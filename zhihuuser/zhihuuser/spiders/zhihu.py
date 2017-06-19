# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    start_user = 'excited-vczh'
    user_url = 'http://www.zhihu.com/api/v4/members/{user}?include={include}'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,'\
                    'employments,answer_count,follower_count,'\
                    'articles_count,gender,badge[?(type=best_answerer)].topics'


    def start_requests(self):
        yield scrapy.Request(url=
                             self.follows_url.format(user=self.start_user, include=self.follows_query, limit=20, offset=0),
                             headers=self.headers,
                             callback=self.follows_parse)
        # yield scrapy.Request(url=self.user_url.format(user=self.start_user,include=self.user_query),
        #                      headers=self.headers,
        #                      callback=self.user_parse)

    def follows_parse(self, response):
        print(response.text)

    def user_parse(self, response):
        print(response.body)
