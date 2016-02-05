#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 20:48:01
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-11 20:51:13

from torndb import Connection
from conf import db.dbConf as dbConf

class BaseModel(object):
	"""docstring for BaseModel"""
	def __init__(self):
		super(BaseModel, self).__init__()
		try:
			conn = Connection(
				host = dbConf['host'],
				database = dbConf['dbname'],
				user = dbConf['user'],
				password = dbConf['pwd']
			)
		except Exception:
			conn = {}
			print 'db connect failed'
	
		self.db = conn