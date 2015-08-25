#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 17:23:27
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-18 18:41:40

from tornado.web import RequestHandler

class HomeHandler(RequestHandler):
	"""docstring for HomeHandler"""
	# def __init__(self, arg = None):
	# 	super(HomeHandler, self).__init__()
	# 	self.arg = arg

	# data api:
	# return data = {
	# 	'success': 1, # 1 for success handle this req, 0 for handle failed
	# 	'msg': 'hande success or failed', # detail handle reason,for debug failed hanle
	# 	'data': {} # data response for request, should be formated in json
	# }
	
	def get(self):
		data = {
			'success': 1,
			'msg': 'get data success',
			'data': {}
		}
		self.write(data)
		self.finish()
	def put(self):
		data = {
			'success': 1,
			'msg': 'put method success',
			'data': {}
		}
		self.write(data)
		self.finish()
	def post(self):
		data = {
			'success': 1,
			'msg': 'post handle success',
			'data': {}
		}
		self.write(data)
		self.finish()
	def delete(self):
		data = {
			'success': 1,
			'msg': 'delete handle success',
			'data': {}
		}