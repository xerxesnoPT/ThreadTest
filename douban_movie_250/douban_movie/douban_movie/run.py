# -*- coding: utf-8 -*-
from scrapy import cmdline
name = 'douban_movie'
cmd = 'scrapy crawl {0} -o moive.csv'.format(name)
cmdline.execute(cmd.split())
