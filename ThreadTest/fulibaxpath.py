# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os
class Fuliba(object):
    def __init__(self,url):
        self.url = url

    def gethtml(self):
        try:
            res = requests.get(self.url)
            res.encoding = 'utf-8'
            return res.text
        except:
            print('get html wrong')

    def getHeadLink(self):
        html = self.gethtml()
        htmlxml = etree.HTML(html)
        headlink = htmlxml.xpath('//*[@id="content"]/article/header/h2/a/@href')
        return headlink


def write2file(alink):
    pname = os.getcwd()
    li = [i +';' for i in alink]
    filename = pname +'/fuliba.txt'
    with open(filename,'w') as f:
        f.writelines(li)


if __name__ == '__main__':
    htmladres = "http://fuliba.net/"
    test = Fuliba(htmladres)
    alink = test.getHeadLink()
    print(alink)
    write2file(alink)

