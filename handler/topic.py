#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import uuid
import hashlib
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
from user import get_user_inv_list

from lib.variables import *
from form.topic import *
from lib.variables import gen_random
from lib.xss import XssCleaner
from lib.utils import find_mentions

class IndexHandler(BaseHandler):
	def get(self, tv = {}):
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

class NodeTopicsHandler(BaseHandler):
	def get(self, node_slug, tv = {}):
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
		tv["topics"] = self.topic_model.get_all_topics_by_node_slug(current_page = page, node_slug = node_slug)
		tv["node"] = self.node_model.get_node_by_node_slug(node_slug)
		tv["active_page"] = "topic"
		tv["gen_random"] = gen_random
		tv["status_counter"] = {
			"topics": len(tv["topics"]["list"]),
		}
		self.render("topic/node_topics.html", **tv)
	def post(self, node_slug):
		user_info = self.current_user
		page = int(self.get_argument("p", "1"))
		data = {}
		data['user_info'] = user_info
		user_counter = self.topic_model.get_user_all_topics_count(user_info["uid"])
		user_replies = self.reply_model.get_user_all_replies_count(user_info["uid"])
		user_favourites = self.favorite_model.get_user_favorite_count(user_info["uid"]);
		if(user_info):
			data['user_info']['counter'] = {
				'topics': user_counter,
				'user_replies': user_replies,
				'user_favourites': user_favourites
			}
			user_notification_count = self.notification_model.get_user_unread_notification_count(user_info["uid"])
			data['notifications_count'] = user_notification_count
		topics = self.topic_model.get_all_topics_by_node_slug(current_page = page, node_slug = node_slug)
		
		for topic in topics['list']:			
			topic['last_touched']  = str(topic['last_touched'])
			topic['last_replied_time'] = str(topic['last_replied_time'])
			topic['created'] = str(topic['created'])
			topic['updated'] = str(topic['updated'])

		node = self.node_model.get_node_by_node_slug(node_slug)
		data['topics'] = topics
		data['gen_random'] = str(gen_random())
		data['status_counter'] = {
			'topics':len(topics['list'])
			#!replies number should be add later!
		}
		data['user_info']['updated'] = str(data['user_info']['updated'])
		data['user_info']['created'] = str(data['user_info']['created'])

		self.write(data)
		self.finish()

class ViewHandler(BaseHandler):
	def get(self, topic_id, tv = {}):
		user_info = self.current_user
		page = int(self.get_argument("p", "1"))
		user_info = self.get_current_user()
		tv["user_info"] = user_info
		if(user_info):
			tv["user_info"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
			}

			tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(user_info["uid"]);
			tv["topic_favorited"] = self.favorite_model.get_favorite_by_topic_id_and_owner_user_id(topic_id, user_info["uid"]);

		tv["gen_random"] = gen_random
		tv["topic"] = self.topic_model.get_topic_by_topic_id(topic_id)

		# check reply count and cal current_page if `p` not given
		reply_num = 106
		reply_count = tv["topic"]["reply_count"]
		reply_last_page = (reply_count / reply_num + (reply_count % reply_num and 1)) or 1
		page = int(self.get_argument("p", reply_last_page))
		tv["reply_num"] = reply_num
		tv["current_page"] = page

		# = self.reply_model.get_all_replies_by_topic_id(topic_id, current_page = page, num = reply_num)

		replies = self.reply_model.get_all_replies_by_topic_id(topic_id, current_page = page, num = reply_num)

		tv["replies"] = replies
		for reply in replies['list']:
			author_inv_list = get_user_inv_list(self, int(reply['author_id']))
			reply['inv_list'] = author_inv_list

		tv["active_page"] = "topic"

		# update topic reply_count and hits

		self.topic_model.update_topic_by_topic_id(topic_id, {
			"reply_count": tv["replies"]["page"]["total"],
			"hits": (tv["topic"]["hits"] or 0) + 1,
		})

		self.render("topic/view.html", **tv)

	@tornado.web.authenticated
	def post(self, tv = {}):
		tv = {}

		# validate the fields

		form = ReplyForm(self)

		if not form.validate():
			self.get(form.tid.data, {"errors": form.errors})
			return

		# continue while validate succeed

		topic_info = self.topic_model.get_topic_by_topic_id(form.tid.data)
		replied_info = self.reply_model.get_user_last_reply_by_topic_id(self.current_user["uid"], form.tid.data)

		if(not topic_info):
			tv["errors"] = {}
			tv["errors"]["invalid_topic_info"] = [u"要回复的帖子不存在"]
			self.get(form.tid.data, tv)
			return

		if(replied_info):
			last_replied_fingerprint = hashlib.sha1(str(replied_info.topic_id) + str(replied_info.author_id) + replied_info.content).hexdigest()
			new_replied_fingerprint = hashlib.sha1(str(form.tid.data) + str(self.current_user["uid"]) + form.content.data).hexdigest()

			if last_replied_fingerprint == new_replied_fingerprint:
				tv["errors"] = {}
				tv["errors"]["duplicated_reply"] = [u"回复重复提交"]
				self.get(form.tid.data, tv)
				return
		
		reply_info = {
			"author_id": self.current_user["uid"],
			"topic_id": form.tid.data,
			# "content": XssCleaner().strip(form.content.data),
			"content": form.content.data,
			"created": time.strftime('%Y-%m-%d %H:%M:%S'),
		}

		reply_id = self.reply_model.add_new_reply(reply_info)

		# update topic last_replied_by and last_replied_time

		self.topic_model.update_topic_by_topic_id(form.tid.data, {
			"last_replied_by": self.current_user["uid"],
			"last_replied_time": time.strftime('%Y-%m-%d %H:%M:%S'),
			"last_touched": time.strftime('%Y-%m-%d %H:%M:%S'),
		})

		# create reply notification

		if not self.current_user["uid"] == topic_info["author_id"]:
			self.notification_model.add_new_notification({
				"trigger_user_id": self.current_user["uid"],
				"involved_type": 1, # 0: mention, 1: reply
				"involved_user_id": topic_info["author_id"],
				"involved_topic_id": form.tid.data,
				"content": form.content.data,
				"status": 0,
				"occurrence_time": time.strftime('%Y-%m-%d %H:%M:%S'),
			})

		# create @username notification

		for username in set(find_mentions(form.content.data)):
			mentioned_user = self.user_model.get_user_by_username(username)

			if not mentioned_user:
				continue

			if mentioned_user["uid"] == self.current_user["uid"]:
				continue

			if mentioned_user["uid"] == topic_info["author_id"]:
				continue

			self.notification_model.add_new_notification({
				"trigger_user_id": self.current_user["uid"],
				"involved_type": 0, # 0: mention, 1: reply
				"involved_user_id": mentioned_user["uid"],
				"involved_topic_id": form.tid.data,
				"content": form.content.data,
				"status": 0,
				"occurrence_time": time.strftime('%Y-%m-%d %H:%M:%S'),
			})

		# update reputation of topic author
		if not self.current_user["uid"] == topic_info["author_id"] and not replied_info:
			topic_time_diff = datetime.datetime.now() - topic_info["created"]
			reputation = topic_info["author_reputation"] or 0
			reputation = reputation + 2 * math.log(self.current_user["reputation"] or 0 + topic_time_diff.days + 10, 10)
			self.user_model.set_user_base_info_by_uid(topic_info["author_id"], {"reputation": reputation})

		# self.get(form.tid.data)
		self.redirect("/t/%s#reply%s" % (form.tid.data, topic_info["reply_count"] + 1))

class CreateHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self, node_slug = None, tv = {}):
		user_info = self.current_user
		tv["user_info"] = user_info
		tv["user_info"]["counter"] = {
			"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
			"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
			"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
		}

		tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(user_info["uid"]);
		tv["gen_random"] = gen_random
		tv["node_slug"] = node_slug
		tv["active_page"] = "topic"
		self.render("topic/create.html", **tv)

	@tornado.web.authenticated
	def post(self, node_slug = None):

		form = CreateForm(self)
		if not form.validate():
			data = {
				'success': 0,
				'msg': form.errors,
				'error': 'form'
			}
			self.finish(data)
			return
		
		node = self.node_model.get_node_by_node_slug(node_slug)
		last_created = self.topic_model.get_user_last_created_topic(self.current_user["uid"])

		if last_created:
			last_created_fingerprint = hashlib.sha1(last_created.title + last_created.content + str(last_created.node_id)).hexdigest()
			new_created_fingerprint = hashlib.sha1(form.title.data + form.content.data + str(node["id"])).hexdigest()

			if last_created_fingerprint == new_created_fingerprint:
				data = {
					'success': 0,
					'msg': '帖子重复提交',
					'error': '帖子重复提交'
				}
				self.finish(data)
				return

		if node is None:
			data = {
				'success': 0,
				'msg': '节点为空，请刷新页面',
				'error': '无效的节点'
			}
		else:
			node_id = node["id"]
			topic_info = {
				"author_id": self.current_user["uid"],
				"title": form.title.data,
				# "content": XssCleaner().strip(form.content.data),
				"content": form.content.data,
				"node_id": node_id,
				"created": time.strftime('%Y-%m-%d %H:%M:%S'),
				"reply_count": 0,
				"last_touched": time.strftime('%Y-%m-%d %H:%M:%S'),
			}
			topic_id = self.topic_model.add_new_topic(topic_info)
			reputation = self.current_user["reputation"] or 0
			reputation = reputation - 5
			reputation = 0 if reputation < 0 else reputation
			self.user_model.set_user_base_info_by_uid(topic_info["author_id"], {"reputation": reputation})
			data = {
				'success': 1,
				'msg': '帖子提交成功',
				'topic_id': topic_id,
				'error': None
			}
		self.write(data)
		self.finish()

class EditHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self, topic_id, tv = {}):
		user_info = self.current_user
		tv["user_info"] = user_info
		tv["user_info"]["counter"] = {
			"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
			"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
			"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
		}

		tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(user_info["uid"]);
		tv["topic"] = self.topic_model.get_topic_by_topic_id(topic_id)
		tv["gen_random"] = gen_random
		tv["active_page"] = "topic"
		self.render("topic/edit.html", **tv)

	@tornado.web.authenticated
	def post(self, topic_id):

		form = CreateForm(self)
		if not form.validate():
			data = {
				'success': 0,
				'msg': form.errors,
				'error': 'form'
			}
			self.finish(data)
			return

		# continue while validate succeed
		topic_info = self.topic_model.get_topic_by_topic_id(topic_id)
		if(not topic_info["author_id"] == self.current_user["uid"]):
			data = {
				'success': 0,
				'msg': '没有权限修改该主题',
				'error': '没有权限修改该主题'
			}
			self.finish(data)
			return

		update_topic_info = {
			"title": form.title.data,
			# "content": XssCleaner().strip(form.content.data),
			"content": form.content.data,
			"updated": time.strftime('%Y-%m-%d %H:%M:%S'),
			"last_touched": time.strftime('%Y-%m-%d %H:%M:%S'),
		}

		reply_id = self.topic_model.update_topic_by_topic_id(topic_id, update_topic_info)

		# update reputation of topic author
		reputation = topic_info["author_reputation"] or 0
		reputation = reputation - 2
		reputation = 0 if reputation < 0 else reputation
		self.user_model.set_user_base_info_by_uid(topic_info["author_id"], {"reputation": reputation})
		data = {
			'success': 1,
			'msg': topic_id,
			'error': None
		}
		self.finish(data)
		return

class ProfileHandler(BaseHandler):
	def get(self, user, tv = {}):
		if(re.match(r'^\d+$', user)):
			user_info = self.user_model.get_user_by_uid(user)
		else:
			user_info = self.user_model.get_user_by_username(user)

		if not user_info:
			self.write_error(404)
			return

		current_user = self.current_user
		page = int(self.get_argument("p", "1"))
		tv["user_info"] = user_info
		if(user_info):
			tv["user_info"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
			}

		if(current_user):
			tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(current_user["uid"]);

		tv["topics"] = self.topic_model.get_user_all_topics(user_info["uid"], current_page = page)
		tv["replies"] = self.reply_model.get_user_all_replies(user_info["uid"], current_page = page)
		tv["gen_random"] = gen_random
		tv["active_page"] = "_blank"
		self.render("topic/profile.html", **tv)

class VoteHandler(BaseHandler):
	def get(self, tv = {}):
		topic_id = int(self.get_argument("topic_id"))
		topic_info = self.topic_model.get_topic_by_topic_id(topic_id)

		if not topic_info:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "topic_not_exist",
			}))
			return

		if self.current_user["uid"] == topic_info["author_id"]:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "can_not_vote_your_topic",
			}))
			return

		if self.vote_model.get_vote_by_topic_id_and_trigger_user_id(topic_id, self.current_user["uid"]):
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "already_voted",
			}))
			return

		self.vote_model.add_new_vote({
			"trigger_user_id": self.current_user["uid"],
			"involved_type": 0, # 0: topic, 1: reply
			"involved_user_id": topic_info["author_id"],
			"involved_topic_id": topic_id,
			"status": 0,
			"occurrence_time": time.strftime('%Y-%m-%d %H:%M:%S'),
		})

		self.write(lib.jsonp.print_JSON({
			"success": 1,
			"message": "thanks_for_your_vote",
		}))

		# update reputation of topic author
		topic_time_diff = datetime.datetime.now() - topic_info["created"]
		reputation = topic_info["author_reputation"] or 0
		reputation = reputation + 2 * math.log(self.current_user["reputation"] or 0 + topic_time_diff.days + 10, 10)
		self.user_model.set_user_base_info_by_uid(topic_info["author_id"], {"reputation": reputation})

class UserTopicsHandler(BaseHandler):
	def get(self, user, tv = {}):
		if(re.match(r'^\d+$', user)):
			user_info = self.user_model.get_user_by_uid(user)
		else:
			user_info = self.user_model.get_user_by_username(user)

		current_user = self.current_user
		page = int(self.get_argument("p", "1"))
		tv["user_info"] = user_info
		if(user_info):
			tv["user_info"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
			}

		if(current_user):
			tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(current_user["uid"]);

		tv["topics"] = self.topic_model.get_user_all_topics(user_info["uid"], current_page = page)
		tv["active_page"] = "topic"
		tv["gen_random"] = gen_random
		self.render("topic/user_topics.html", **tv)

class UserRepliesHandler(BaseHandler):
	def get(self, user, tv = {}):
		if(re.match(r'^\d+$', user)):
			user_info = self.user_model.get_user_by_uid(user)
		else:
			user_info = self.user_model.get_user_by_username(user)

		current_user = self.current_user
		page = int(self.get_argument("p", "1"))
		tv["user_info"] = user_info
		if(user_info):
			tv["user_info"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
			}

		if(current_user):
			tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(current_user["uid"]);

		tv["replies"] = self.reply_model.get_user_all_replies(user_info["uid"], current_page = page)
		tv["active_page"] = "topic"
		tv["gen_random"] = gen_random
		self.render("topic/user_replies.html", **tv)

class UserFavoritesHandler(BaseHandler):
	def get(self, user, tv = {}):
		if(re.match(r'^\d+$', user)):
			user_info = self.user_model.get_user_by_uid(user)
		else:
			user_info = self.user_model.get_user_by_username(user)

		current_user = self.current_user
		page = int(self.get_argument("p", "1"))
		tv["user_info"] = user_info
		if(user_info):
			tv["user_info"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
			}

		if(current_user):
			tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(current_user["uid"]);

		tv["favorites"] = self.favorite_model.get_user_all_favorites(user_info["uid"], current_page = page)
		tv["active_page"] = "topic"
		tv["gen_random"] = gen_random
		self.render("topic/user_favorites.html", **tv)

class ReplyEditHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self, reply_id, tv = {}):
		user_info = self.current_user
		tv["user_info"] = user_info
		tv["user_info"]["counter"] = {
			"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
			"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
			"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
		}

		tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(user_info["uid"]);
		tv["reply"] = self.reply_model.get_reply_by_reply_id(reply_id)
		tv["gen_random"] = gen_random
		tv["active_page"] = "topic"
		self.render("topic/reply_edit.html", **tv)

	@tornado.web.authenticated
	def post(self, reply_id, tv = {}):
		tv = {}

		# validate the fields

		form = ReplyEditForm(self)

		if not form.validate():
			self.get(reply_id, {"errors": form.errors})
			return

		# continue while validate succeed

		reply_info = self.reply_model.get_reply_by_reply_id(reply_id)

		if(not reply_info["author_id"] == self.current_user["uid"]):
			tv["errors"] = {}
			tv["errors"]["invalid_permission"] = [u"没有权限修改该回复"]
			self.get(reply_id, tv)
			return

		update_reply_info = {
			# "content": XssCleaner().strip(form.content.data),
			"content": form.content.data,
			"updated": time.strftime('%Y-%m-%d %H:%M:%S'),
		}

		reply_id = self.reply_model.update_reply_by_reply_id(reply_id, update_reply_info)

		# update reputation of topic author
		reputation = self.current_user["reputation"] or 0
		reputation = reputation - 2
		reputation = 0 if reputation < 0 else reputation
		self.user_model.set_user_base_info_by_uid(reply_info["author_id"], {"reputation": reputation})
		self.redirect("/t/%s" % reply_info["topic_id"])

class FavoriteHandler(BaseHandler):
	def get(self, tv = {}):
		topic_id = int(self.get_argument("topic_id"))
		topic_info = self.topic_model.get_topic_by_topic_id(topic_id)

		if not self.current_user:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "user_not_login",
			}))
			return

		if not topic_info:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "topic_not_exist",
			}))
			return

		if self.current_user["uid"] == topic_info["author_id"]:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "can_not_favorite_your_topic",
			}))
			return

		if self.favorite_model.get_favorite_by_topic_id_and_owner_user_id(topic_id, self.current_user["uid"]):
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "already_favorited",
			}))
			return

		self.favorite_model.add_new_favorite({
			"owner_user_id": self.current_user["uid"],
			"involved_type": 0, # 0: topic, 1: reply
			"involved_topic_id": topic_id,
			"created": time.strftime('%Y-%m-%d %H:%M:%S'),
		})

		self.write(lib.jsonp.print_JSON({
			"success": 1,
			"message": "favorite_success",
		}))

		# update reputation of topic author
		topic_time_diff = datetime.datetime.now() - topic_info["created"]
		reputation = topic_info["author_reputation"] or 0
		reputation = reputation + 2 * math.log(self.current_user["reputation"] or 0 + topic_time_diff.days + 10, 10)
		self.user_model.set_user_base_info_by_uid(topic_info["author_id"], {"reputation": reputation})

class CancelFavoriteHandler(BaseHandler):
	def get(self, tv = {}):
		topic_id = int(self.get_argument("topic_id"))
		topic_info = self.topic_model.get_topic_by_topic_id(topic_id)
		favorite_info = None

		if not self.current_user:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "user_not_login",
			}))
			return

		if not topic_info:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "topic_not_exist",
			}))
			return

		favorite_info = self.favorite_model.get_favorite_by_topic_id_and_owner_user_id(topic_id, self.current_user["uid"])

		if not favorite_info:
			self.write(lib.jsonp.print_JSON({
				"success": 0,
				"message": "not_been_favorited",
			}))
			return

		self.favorite_model.cancel_exist_favorite_by_id(favorite_info["id"])

		self.write(lib.jsonp.print_JSON({
			"success": 1,
			"message": "cancel_favorite_success",
		}))

		# update reputation of topic author
		topic_time_diff = datetime.datetime.now() - topic_info["created"]
		reputation = topic_info["author_reputation"] or 0
		reputation = reputation + 2 * math.log(self.current_user["reputation"] or 0 + topic_time_diff.days + 10, 10)
		self.user_model.set_user_base_info_by_uid(topic_info["author_id"], {"reputation": reputation})

class MembersHandler(BaseHandler):
	def get(self, tv = {}):
		user_info = self.current_user
		tv["user_info"] = user_info
		if(user_info):
			tv["user_info"]["counter"] = {
				"topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
				"replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
				"favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
			}

			tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(user_info["uid"]);

		tv["members"] = self.user_model.get_users_by_latest(num = 49)
		tv["active_members"] = self.user_model.get_users_by_last_login(num = 49)
		tv["gen_random"] = gen_random
		tv["active_page"] = "members"
		self.render("topic/members.html", **tv)

