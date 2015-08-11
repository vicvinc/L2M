#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sguar
# @Date:   2015-08-08 15:48:22
# @Last Modified by:   Sguar
# @Last Modified time: 2015-08-08 16:07:44

import uuid
import StringIO
import time
import json
import re
import tornado.web
import lib.jsonp
import pprint
import math
import datetime

from base import *
from lib.variables import *
from form.topic import *
from lib.variables import gen_random
from lib.utils import find_mentions

class HomeHandler(BaseHandler):
	"""docstring for HomeHandler"""
	# def __init__(self, arg):
	# 	super(HomeHandler, self).__init__()
	# 	self.arg = arg
	def get(self, *argvs):
		uinfo = self.current_user
		page = int(self.get_argument("p", "1"))
		data = {}
		data["uinfo"] = uinfo
		if(uinfo):
			data["uinfo"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(uinfo["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(uinfo["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(uinfo["uid"]),
			}

			data["notifications_count"] = self.notification_model.get_user_unread_notification_count(uinfo["uid"]);

		data["status_counter"] = {
			"users": self.user_model.get_all_users_count(),
			"nodes": self.node_model.get_all_nodes_count(),
			"topics": self.topic_model.get_all_topics_count(),
			"replies": self.reply_model.get_all_replies_count(),
		}
		data["topics"] = self.topic_model.get_all_topics(current_page = page)
		data["planes"] = self.plane_model.get_all_planes_with_nodes()
		data["allnodes"] = self.node_model.get_all_nodes()
		data["hot_nodes"] = self.node_model.get_all_hot_nodes()
		data["active_page"] = "home"
		data["gen_random"] = gen_random
		self.render("home/index.html", **data)
