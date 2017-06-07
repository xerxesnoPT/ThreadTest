# -*- coding: utf-8 -*-
import requests
import threading
from threading import Thread
from lxml import etree
class GetPhoto(object):
    def __init__(self,url):
        self.url = url
    def gethtml(self):
        try:
            res = requests.get(self.url)
            res.encoding = res.apparent_encoding
            return res.text
        except:
            return 'open url wrong'

    def GetPhoto(self):
        html = self.gethtml()
        selection = etree.HTML(html)
        photolist = selection.xpath('//*[@id="43813"]/div[3]/p/strong/img/@src')
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


# class MyThread(Thread):
#     def __init__(self, savfile,address):
#         super(MyThread,self).__init__()
#         self.savfile = savfile
#         self.address = address
#     def run(self):
#         downthread = GetPhoto(self.address)
#         downthread.Download(self.savfile)






        # // *[ @ id = "43813"] / div[3] / p[25] / strong / img
        # // *[ @ id = "43813"] / div[3] / p[49] / strong / img

if __name__ == '__main__':
    address = 'http://fuliba.net/%E9%BB%91%E8%89%B2%E6%81%8B%E6%83%85.html'
    savadress = 'f:/fuliba/phot'
    test = GetPhoto(address)
    test.Download(savadress)
    # t1 = MyThread(address, 'f:/fuliba/phot')
    # t2 = MyThread(address, 'f:/fuliba/phot')
    # t1.start()
    # t2.start()
