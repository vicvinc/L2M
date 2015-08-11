#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

# cat /etc/mime.types
# application/octet-stream    crx

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import os.path
import re
import memcache
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import handler.base
import handler.user
import handler.node
import handler.topic
import handler.page
import handler.notification
import handler.panel
import handler.index

from tornado.options import define, options
from lib.loader import Loader
from lib.session import Session, SessionManager
from jinja2 import Environment, FileSystemLoader
from conf import routes

define("port", default = 80, help = "run on the given port", type = int)
define("mysql_host", default = "mysql_host", help = "community database host")
define("mysql_database", default = "mysql_db_name", help = "community database name")
define("mysql_user", default = "mysql_db_user", help = "community database user")
define("mysql_password", default = "mysql_db_password", help = "community database password")

class Application(tornado.web.Application):
	def __init__(self):
		settings = dict(
			blog_title = u"Dota2Ark Community",
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			avatar_path = os.path.join(os.path.dirname(__file__), 'static/avatar'),
			xsrf_cookies = True,
			cookie_secret = "cookie_secret_code",
			login_url = "/login",
			autoescape = None,
			jinja2 = Environment(loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")), trim_blocks = True),
			reserved = ["user", "topic", "home", "setting", "forgot", "login", "logout", "register", "admin"],
			# debug = True,
		)

		tornado.web.Application.__init__(self, routes, **settings)

		# Have one global connection to the blog DB across all handlers
		self.db = torndb.Connection(
			host = options.mysql_host, database = options.mysql_database,
			user = options.mysql_user, password = options.mysql_password
		)

		# Have one global loader for loading models and handles
		self.loader = Loader(self.db)

		# Have one global model for db query
		self.user_model = self.loader.use("user.model")
		self.topic_model = self.loader.use("topic.model")
		self.reply_model = self.loader.use("reply.model")
		self.plane_model = self.loader.use("plane.model")
		self.node_model = self.loader.use("node.model")
		self.notification_model = self.loader.use("notification.model")
		self.vote_model = self.loader.use("vote.model")
		self.favorite_model = self.loader.use("favorite.model")

		self.panel_model = self.loader.use('panel.model')
		self.item_model = self.loader.use('item.model')
		self.inventory_model = self.loader.use('inventory.model')
		# Have one global session controller
		self.session_manager = SessionManager(settings["cookie_secret"], ["127.0.0.1:11211"], 0)

		# Have one global memcache controller
		self.mc = memcache.Client(["127.0.0.1:11211"])

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()

