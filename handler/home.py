#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 17:23:27
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-11 20:58:52

from tornado.web import RequestHandler

class HomeHandler(RequestHandler):
	"""docstring for HomeHandler"""
	# def __init__(self, arg = None):
	# 	super(HomeHandler, self).__init__()
	# 	self.arg = arg
	def get(self):
		data = 'hell tornado!'
		self.write(data)
		self.finish()
		