#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-06 17:10:26
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-10 11:05:45
import newspaper
import sys, os, json
from pprint import pprint

class news(object):
	"""docstring for news"""
	def __init__(self, arg):
		super(news, self).__init__()
		if (arg.title):
			self.title = arg.title
		if (arg.content):
			self.content = arg.content
		if (arg.author):
			self.author = arg.author
		if (arg.date):
			self.date = arg.date
		if (arg.source):
			self.date = arg.source
		if (arg.srcurl):
			self.srcurl = arg.srcurl
	def save(self):
		return
def newSource():
	src = [
		{
			'name': 'wanmei',
			'url': 'http://www.dota2.com.cn/news/'
		},{
			'name': 'steam',
			'url': 'http://www.dota2.com'
		}
	]
	return src;

if __name__ == '__main__':
	src = newSource()
	for s in src:
		pprint(s)
		d2news = newspaper.build( s['url'], language = 'zh' )
		f = open('aritcle.json', 'w')
		for a in d2news.articles:
			a.download()
			a.parse()

			try:
				pprint(a)
				article = {}
				article.title = a.title
				article.url = a.url
				article.content = a.text
				article.summary = a.summary
				article.author = str(a.authors)

				f.write(json_encode(article))

				pprint(a.url)
				print(a.text[:150])
			except Exception, e:
				raise e
		f.close()