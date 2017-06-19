# -*- coding: utf-8 -*-
class Url_manger(object):
    def __init__(self):
        self.spider_url = set()
        self.crawled_url = set()
    def add_url(self,url):
        if  url not in self.spider_url and url not in self.crawled_url:
            self.spider_url.append(url)


    def get_url(self):
        newurl = self.spider_url.pop()
        self.crawled_url


