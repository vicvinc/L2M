#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-10 11:17:04
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-10 11:18:54

import scrapy

class wanmeiSpider(scrapy.Spider):
	name = 'wanmei'
	allowed_domains = ['dmoz.org']
	start_urls = [
		'http://www.dota2.com.cn',
		'http://www.dota2.com.cn/news/'
	]

	def parse(self, response):
		filename = response.url.split('/')[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)