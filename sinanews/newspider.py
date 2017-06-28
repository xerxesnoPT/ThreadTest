# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymongo
import re

class News_crawl(object):
    def __init__(self):
        self.title = ''
        self.href = ''
        db = pymongo.MongoClient()
        self.mongo_collection = db['sinanews']['info']

    def _gethtml(self,url):
        try:
            res = requests.get(url)
            res.encoding = 'utf-8'
            res.raise_for_status()
            return res.text
        except:
            print('html解析错误')

    def _getsoup(self,url):
        try:
            soup = BeautifulSoup(self._gethtml(url),'lxml')
            return soup
        except:
            print('soup wrong')

    def main_crawl(self,url):
        text = []
        soup = self._getsoup(url)
        self.title = soup.find('h1', id='j_title').get_text()
        div = soup.find('div',class_='article-a__content')
        for child in div.children:
            if child.name == 'figure':
                href = child.img['src']
                text.append(child.img['src'])
                # text.append(requests.get(href).content)
            elif child.name == 'p':
                text.append('\n'+child.string+'\n')
        print(text)
        post = {'_id': self.title,'内容':text}
        self.mongo_collection.save(post)
        # with open('ab.txt', 'w') as f:
            # f.writelines(text)

        # dr = re.compile(r'<[^>]+>', re.S)
            # s = dr.sub('',child)
        # for string in div.stripped_strings:
        #     print(string)


if __name__ == '__main__':
    url = 'http://sports.sina.com.cn/g/pl/2017-06-28/doc-ifyhmtek7898466.shtml'
    test = News_crawl()
    test.main_crawl(url)
