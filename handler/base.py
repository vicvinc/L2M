#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import tornado.web
import lib.session
import time
import helper

class BaseHandler(tornado.web.RequestHandler):
	def __init__(self, *argc, **argkw):
		super(BaseHandler, self).__init__(*argc, **argkw)
		self.session = lib.session.Session(self.application.session_manager, self)
		self.jinja2 = self.settings.get("jinja2")
		self.jinja2 = helper.Filters(self.jinja2).register()
	def write_error(self, status_code, **argkw):
		if status_code == 404:
			self.render('snippet/404.html',page=None)
		else:
			self.render('snippet/unknow.html',page=None)
	@property
	def db(self):
		return self.application.db

	@property
	def user_model(self):
		return self.application.user_model

	@property
	def topic_model(self):
		return self.application.topic_model

	@property
	def reply_model(self):
		return self.application.reply_model

	@property
	def plane_model(self):
		return self.application.plane_model
	#add  model
	@property
	def panel_model(self):
		return self.application.panel_model

	@property
	def item_model(self):
		return self.application.item_model

	@property
	def inventory_model(self):
	    return self.application.inventory_model
	
	#end  model
	@property
	def node_model(self):
		return self.application.node_model

	@property
	def notification_model(self):
		return self.application.notification_model

	@property
	def vote_model(self):
		return self.application.vote_model

	@property
	def favorite_model(self):
		return self.application.favorite_model

	@property
	def loader(self):
		return self.application.loader

	@property
	def mc(self):
		return self.application.mc

	def get_current_user(self):
		user_id = self.get_secure_cookie("user")
		if not user_id: return None
		return self.user_model.get_user_by_uid(int(user_id))

	def render(self, template_name, **tv):
		html = self.render_string(template_name, **tv)
		self.write(html)

	def render_string(self, template_name, **tv):
		tv["xsrf_form_html"] = self.xsrf_form_html
		tv["current_user"] = self.current_user
		tv["request"] = self.request
		tv["request_handler"] = self
		template = self.jinja2.get_template(template_name)
		return template.render(**tv)

	def render_from_string(self, template_string, **tv):
		template = self.jinja2.from_string(template_string)
		return template.render(**tv)
