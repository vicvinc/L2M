#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vicvinc
# @Date:   2015-07-20 10:22:45
# @Last Modified by:   Sguar
# @Last Modified time: 2015-07-30 18:30:02

import uuid
import hashlib
import StringIO
import time
import json
import re
import urllib2
import tornado.web
import lib.jsonp
import pprint
import math
import datetime

from base import *
from lib.variables import *
from form.topic import *
from form.panel import *
from lib.variables import gen_random
from lib.xss import XssCleaner
from lib.utils import find_mentions

class PanelHandler(BaseHandler):
	'''docstring for ViewPanelHandler'''
	@tornado.web.authenticated
	def get(self, panel_name = None, tv = {}):
		user_info = self.current_user
		tv['user_info'] = user_info
		tv['user_info']['counter'] = {
			'topics': self.topic_model.get_user_all_topics_count(user_info['uid']),
			'replies': self.reply_model.get_user_all_replies_count(user_info['uid']),
			'favorites': self.favorite_model.get_user_favorite_count(user_info['uid']),
		}
		tv['notifications_count'] = self.notification_model.get_user_unread_notification_count(user_info['uid']);
		tv['gen_random'] = gen_random
		tv['active_page'] = 'topic'
		tv['panels'] = self.panel_model.get_all_panels()
		self.render('panel/index.html', **tv)
	@tornado.web.authenticated
	def post(self, panel_name = None, tv = {}):
		tv = {}
		# validate the fieldes
		form = CreateForm(self)
		if not form.validate():
			self.get( panel_name, {"errors": form.errors})
			return
		# continue while validate succeed
		panel = self.panel_model.get_panel_by_panel_name(panel_name)
		last_created = self.panel_model.get_panel_by_user_last_created(self.current_user["uname"])
		if last_created:
			last_created_fingerprint = hashlib.sha1(last_created.name + str(last_created.panel_id)).hexdigest()
			new_created_fingerprint = hashlib.sha1(form.title.data + str(panel["id"])).hexdigest()
			if last_created_fingerprint == new_created_fingerprint:
				tv["errors"] = {}
				tv["errors"]["duplicated_topic"] = [u"面板重复提交"]
				self.get(panel_name, tv)
				return
		if panel is None:
			print "did find panel by user name plz check db table panel"
			panel_id = int(time.time())
		else:
			panel_id = panel["id"]

		p_info = {
			"owner": self.current_user["uname"],
			"name": form.title.data,
			"describe": form.content.data,
			"created": time.strftime('%Y-%m-%d %H:%M:%S'),
			"updated": time.strftime('%Y-%m-%d %H:%M:%S'),
		}

		panel_id = self.panel_model.add_new_panel(p_info)

		# update reputation of topic author
		reputation = self.current_user["reputation"] or 0
		reputation = reputation + 5
		reputation = 0 if reputation < 0 else reputation
		self.user_model.set_user_base_info_by_uid(topic_info["author_id"], {"reputation": reputation})
		self.redirect("/")
class CreatePanelHandler(BaseHandler):
	'''docstring for panelHandler'''
	@tornado.web.authenticated
	# def __init__(self, tv = {}):
	# 	super(panelHandler, self).__init__()
	def get(self, panel_name = None, tv = {}):
		user_info = self.current_user
		tv['user_info'] = user_info
		tv['user_info']['counter'] = {
			'topics': self.topic_model.get_user_all_topics_count(user_info['uid']),
			'replies': self.reply_model.get_user_all_replies_count(user_info['uid']),
			'favorites': self.favorite_model.get_user_favorite_count(user_info['uid']),
		}

		tv['notifications_count'] = self.notification_model.get_user_unread_notification_count(user_info['uid']);
		tv['gen_random'] = gen_random
		tv['node_slug'] = node_slug
		tv['active_page'] = 'topic'
		self.render('panel/create.html', **tv)
class PanelTopicsHandler(BaseHandler):
	"""docstring for PanelTopicsHandler"""
	def get(self, panel_name, tv = {}):
		user_info = self.current_user
		page = int(self.get_argument("p", "1"))
		tv["user_info"] = user_info
		if(user_info):
			tv["user_info"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
			}
			tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(user_info["uid"]);
		tv["status_counter"] = {
			"users": self.user_model.get_all_users_count(),
			"nodes": self.node_model.get_all_nodes_count(),
			"topics": self.topic_model.get_all_topics_count(),
			"replies": self.reply_model.get_all_replies_count(),
		}
		tv["topics"] = self.topic_model.get_all_topics(current_page = page)
		tv["planes"] = self.plane_model.get_all_planes_with_nodes()
		tv["allnodes"] = self.node_model.get_all_nodes()
		tv["hot_nodes"] = self.node_model.get_all_hot_nodes()
		tv["active_page"] = "topic"
		tv["gen_random"] = gen_random
		self.render("topic/topics.html", **tv)

		

