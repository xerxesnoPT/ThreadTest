# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import random
import datetime

def getHtml(url):
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        return res.text
    except:
        return 'gethtml wrong'


# def getSoup(url):
#     html = getHtml(url)
#     bsobj = BeautifulSoup(html, 'lxml')
#     # green = bsobj.findAll('span', attrs={'class': 'green'})
#     namelist = bsobj.find_all(text='the prince')
#     return namelist


def getSoup(url):
    html = getHtml(url)
    bsobj = BeautifulSoup(html, 'lxml')
    itemlist = bsobj.find_all('a', href=re.compile(r'\/item\/.*'))
    return itemlist


def getItem(url):
    itemlist = getSoup(url)
    random.seed(datetime.datetime.now())
    if len(itemlist) > 0:
        new_item = itemlist[random.randint(0, len(itemlist))].attrs['href']
        print('http://baike.baidu.com'+new_item)
        getItem(new_item)



if __name__ == '__main__':
    pages=set()
    url = 'http://baike.baidu.com/item/%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85/8702'
    def printurl(url):
        bsobj = BeautifulSoup(requests.get(url).text,'lxml')
        global pages
        for i in bsobj.find_all('a', href= re.compile(r'\/item\/.*')):
            if 'href' in i.attrs:
                newurl = 'http://baike.baidu.com' + i.attrs['href']
                if newurl not in pages:
                    pages.add(newurl)
                    print(newurl)
                    printurl(newurl)





