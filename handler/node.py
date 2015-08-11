#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-07 16:22:42
# @Last Modified by:   Sguar
# @Last Modified time: 2015-08-08 16:41:44

import tornado.web
import json
import time

from base import *
# from form.topic import *
from lib.variables import gen_random
from pprint import pprint
from datetime import datetime

class HomeHandler(BaseHandler):
	"""docstring for HomeHandler"""
	def get(self):
		data = {}
		tv = {}
		page = int(self.get_argument("p", "1"))
		tv["topics"] = self.topic_model.get_all_topics(current_page = page)
		tv["gen_random"] = gen_random
		tv["status_counter"] = {
			"topics": len(tv["topics"]["list"]),
		}
		tv['allnodes'] = self.node_model.get_all_nodes()
		tv["active_page"] = "node"
		html = self.render_string("node/index.html", **tv)
		data['html'] = html
		self.write(html)
		self.flush()
		self.finish()
		return
		
class NodeTopicsHandler(BaseHandler):
	"""docstring for NodeTopicsHandler"""
	def get(self, node_slug):
		data = {}
		tv = {}
		if(node_slug is None):
			node_slug = 'default'
		page = int(self.get_argument("p", "1"))
		tv["topics"] = self.topic_model.get_all_topics_by_node_slug(current_page = page, node_slug = node_slug)
		tv["active_page"] = "topic"
		tv["gen_random"] = gen_random
		tv["status_counter"] = {
			"topics": len(tv["topics"]["list"]),
		}
		html = self.render_string("node/nodeitem.html", **tv)
		data['html'] = html
		self.write(data)
		self.flush()
		self.finish()
		return

