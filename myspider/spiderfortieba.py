#-*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#得到html页面
def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding ='utf8'
        return r.text
    except:
        return 'Some thing Wrong'

def getsoup(url):
    #定义一个列表存放爬到到每条数据
    comtexts = []
    html = gethtmltext(url)
    soup = BeautifulSoup(html,'lxml')
    #通过贴吧页面分析发现每个帖子都在li标签中。class属性如下
    lilist = soup.find_all('li',attrs={'class':" j_thread_list clearfix"})
    #遍历每个帖子，定义一个字典用于存放帖子到信息
    for li in lilist:
        comtext = {}
        try:
            #标题直接在a标签的text中
            comtext['title'] = li.find(
                'a',attrs={'class':'j_th_tit '}).text.strip()
            #超链接需要用tieba到前缀拼接,后缀在a标签到href属性中
            comtext['link'] = "http://tieba.baidu.com" + li.find(
                'a',attrs={'class':'j_th_tit '})['href']
            comtext['name'] = li.find(
                'span',attrs={'class':'tb_icon_author'})['title']
            comtext['relyname'] = li.find(
                'span',attrs={'class':'tb_icon_author_rely j_replyer'})['title']
            comtext['time'] = li.find(
                'span',attrs={'class':"threadlist_reply_date pull_right j_reply_data"}).text.strip()
            comtexts.append(comtext)
        except:
            return '解析错误'
    return comtexts

#定义一个函数用于把getsoup函数返回到帖子信息列表写入到本地文件nctieba.txt中.
def write2file(comtexts):
    with open('nctieba.txt','a+') as file:
        for item in comtexts:
            file.write('标题：%s \t 链接：%s\t %s\t %s\t %s\t \n'%(
                item['title'],item['link'],item['name'],item['relyname'],item['time']))
        print('爬取完成')


#定义一个函数用于对tieba地址的页数进行解析
def page_url(base_url,page):
    url_list=[]
    for i in range(0,page):
        url_list.append(base_url+'&pn='+str(50*page))
    return url_list
    #通过分析发现tieba每页显示50条记录，在&pn= 参数后即为页码*50
   # baseurl = 'http://tieba.baidu.com/f?kw=%E5%8D%97%E5%B7%9D&ie=utf-8k'
   # return baseurl+'&pn='+str(50*page)





if __name__=='__main__':
    base_url = 'http://tieba.baidu.com/f?kw=%CB%D5%D6%DD%B4%F3%D1%A7&ie=utf-8'
    url_list = page_url(base_url,page=1)
    for url in url_list:
        comtext = getsoup(url)
        write2file(comtext)


