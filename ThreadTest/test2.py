#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
def gethtml(ads):
    r = requests.get(ads)
    r.encoding = r.apparent_encoding
    return r.text



if __name__ =='__main__':
    ads = 'http://www.baidu.com'
    html = gethtml(ads)
    bs = BeautifulSoup(html,'lxml')
    print(bs)
