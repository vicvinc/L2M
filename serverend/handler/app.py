#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 20:06:38
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-11 21:11:39

# import logging # log system will be added later

from tornado.web import Application
from torndb import Connection
from pprint import pprint
class App(Application):
	"""docstring for App"""
	def __init__(self, appConf):
		if(appConf):
			pprint(appConf.routes)
			super(App, self).__init__(appConf.routes)
		else:
			print 'appConf is None'
		