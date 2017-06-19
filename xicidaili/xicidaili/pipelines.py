# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import xicidaili.settings
from twisted.internet import defer
from twisted.enterprise import adbapi
from scrapy.exceptions import NotConfigured
class XicidailiPipeline(object):
    collection_name = 'XicidailiItem'
    def __init__(self,dbconn):
        self.dbpool = dbconn
    @classmethod
    def from_settings(cls,settings):
        dbargs=dict(host=settings['MYSQL_HOST'],
                user=settings['MYSQL_UNAME'],
                db=settings['MYSQL_DBNAME'],
                port=settings['MYSQL_PORT'],
                passwd=settings['MYSQL_PASSWORD'],
                charset ='utf8')
        dbconn=pymysql.connect(**dbargs)
        return cls(dbconn)

    def process_item(self, item, spider):
        cursor = self.dbpool.cursor()
        sql = 'insert into proxyip (address,ip,type,port) values(%s,%s,%s,%s)'
        try:
            effect_row = cursor.execute(sql,(item['address'],item['ip'],item['type'],item['port']))
            self.dbpool.commit()
        except Exception as e:
            print(e)
            self.dbpool.rollback
        return item


