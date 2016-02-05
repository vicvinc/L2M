#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 11:07:03
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-11 20:05:22

from handler import home
from tornado.web import StaticFileHandler
import app

appConf = app.appConf

routes = [
	(r'/', home.HomeHandler),
	# static handler
	(r'/(favicon\.ico)', StaticFileHandler, appConf['pub']),
	(r'/pub/(.*)', StaticFileHandler, appConf['pub']),
]
