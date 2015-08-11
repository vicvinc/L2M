#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-06 17:10:26
# @Last Modified by:   Sguar
# @Last Modified time: 2015-08-08 19:24:36
import newspaper

from pprint import pprint
class d2news(object):
	"""docstring for d2news"""
	def __init__(self, url):
		pprint(url)
		super(d2news, self).__init__()
		# self.arg = arg
		self.url = url

	def getNews(self):
		self.news = newspaper.build(self.url)
		
	def printNews(self):
		for article in self.news.articles:
			pprint(articles.url)
			a = Article(articles.url, language = 'zh')
			a.download()
			a.parse()
			print(a.text[:150])
		return

if __name__ == '__main__':
	urls = [
		'http://www.dota2.com.cn/news/gamenews/',
		'http://cn.dota2.com/'
	]
	d2news = newspaper.build('http://cn.dota2.com/', language = 'zh')
	for a in d2news.articles:
		pprint(a.url)
		a.download()
		a.parse()
		print(a.text[:150])