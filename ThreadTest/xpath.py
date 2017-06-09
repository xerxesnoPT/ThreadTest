# -*- coding: utf-8 -*-
import requests
import threading
import os
from threading import Thread
from lxml import etree
class GetPhoto(object):
    def __init__(self,url):
        self.url = url
    def gethtml(self):
        try:
            res = requests.get(self.url)
            res.encoding = 'utf-8'
            return res.text
        except:
            return 'open url wrong'

    def GetDownName(self):
        html = self.gethtml()
        selection = etree.HTML(html)
        downname = selection.xpath('//*[@class="entry-common"]/header/h2/text()')
        return downname[0].strip()

    def GetPhoto(self):
        html = self.gethtml()
        selection = etree.HTML(html)
        photolist = selection.xpath('//*[@class="entry-common"]/div[3]/p/strong/img/@src')
        return photolist

    def Download(self,saveadrs):
        urllist = self.GetPhoto()
        i = 1
        for url in urllist:
            strname = saveadrs+'/'+str(i)+url[-4:]
            with open(strname, 'wb') as f:
                f.write(requests.get(url).content)
            i+=1
        print('下载完成')


class MyThread(Thread):
    def __init__(self, address):
        Thread.__init__(self)
        self.address = address
    def run(self):
        downthread = GetPhoto(self.address)
        filename = downthread.GetDownName()
        if not os.path.exists(filename):
            os.system('mkdir %s'%filename)
            downthread.Download(filename)


        # downthread.Download(self.savfile)







        # // *[ @ id = "43813"] / div[3] / p[25] / strong / img
        # // *[ @ id = "43813"] / div[3] / p[49] / strong / img

if __name__ == '__main__':
    # address = 'http://fuliba.net/%E9%BB%91%E8%89%B2%E6%81%8B%E6%83%85.html'
    # address1 = 'http://fuliba.net/%E6%BC%AB%E7%94%BB%E5%96%B5.html'
    htmladdress = input('输入要爬取的福利吧网址,多个网址按;分割:')
    htmllist = htmladdress.split(';')
    # test = GetPhoto(htmladdress)
    # filename = test.GetDownName()
    # print(filename)
    # if not os.path.exists(filename):
    #     os.system('mkdir %s'%filename)
    #     test.Download(filename)
    # test.Download(savadress1)
    # t1 = MyThread(address, savadress)
    # t2 = MyThread(address1, savadress1)
    # t1.start()
    # t2.start()
    threadlist =[]
    for adres in htmllist:
        t = MyThread(adres)
        t.start()





