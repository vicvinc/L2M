#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 11:07:03
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-11 21:08:30

#tornado import
# import tornado.ioloop
# import tornado.web
import torndb
import tornado.template
from tornado.web import Application,RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

#libs import
from pprint import pprint

#package import

#local import
from conf import app as appConf
from handler import app as appservice

def server(appConf):
	port = appConf.appConf['port']

	app = appservice.App(appConf)

	sockets = tornado.netutil.bind_sockets(port)
	#tornado.process.fork_processes(0)
	server = HTTPServer(app)
	server.add_sockets(sockets)

	print 'start service on:', port	
	IOLoop.current().start()

if __name__ == '__main__':
	pprint(dir(appConf))
	server(appConf)

