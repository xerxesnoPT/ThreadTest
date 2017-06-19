# -*- coding: utf-8 -*-
import pymysql
import requests
class Ip_test(object):
    conndict=dict(host='127.0.0.1', user='root',
                  passwd='root', port=3306,db='proxyip',
                  charset='utf8')
    def __init__(self):
        self.dpcon = pymysql.connect(**self.conndict)

    def getip(self):
        dbcursor = self.dpcon.cursor(cursor=pymysql.cursors.DictCursor)
        #游标设置为字典类型，下面返回iplist与数据库列相关联
        sql = 'select * from proxyip'
        try:
            dbcursor.execute(sql)
            iplist = dbcursor.fetchall()
        except Exception as e:
            print(e)
        return iplist



    def iphaswork(self):
        iplist = self.getip()
        https_url = 'https://www.baidu.com'
        http_url = 'http://www.baidu.com'
        for ip in iplist:
            url = http_url if ip['type'].lower =='http' else https_url
            proxyip = ip['type'].lower()+'://'+ip['ip']+':'+ip['port']
            proxydict = {ip['type'].lower():proxyip}
            try:
                html = requests.get(url, timeout=2, proxies=proxydict)
            except:
                cursor = self.dpcon.cursor()
                sql = 'delete from proxyip where id = %s'
                cursor.execute(sql, (ip['id']))
                self.dpcon.commit()




if __name__ == '__main__':
    test = Ip_test()
    test.iphaswork()
