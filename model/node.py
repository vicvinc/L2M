#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import time
from lib.query import Query

class NodeModel(Query):
	def __init__(self, db):
		self.db = db
		self.table_name = "node"
		super(NodeModel, self).__init__()

	def get_all_nodes(self):
		return self.select()

	def get_all_nodes_count(self):
		return self.count()

	def get_nodes_by_plane_id(self, plane_id):
		where = "plane_id = %s" % plane_id
		return self.where(where).select()

	def get_node_by_node_slug(self, node_slug):
		where = "slug = '%s'" % node_slug
		return self.where(where).find()

	def get_all_hot_nodes(self):
		where = "topic.reply_count > 0"
		join = "LEFT JOIN topic ON node.id = topic.node_id"
		order = "topic.reply_count DESC"
		group = "node.id"
		return self.where(where).join(join).order(order).group(group).limit(16).select()
	def add_new_node(self, info):
		'''
		{
			"id": x,
			`name` text,
			`slug` text,
			`thumb` text,
			`introduction` text,
			`created` text,
			`updated` text,
			`plane_id` int(11) DEFAULT NULL,
			`topic_count` int(11) DEFAULT NULL,
			`custom_style` text,
			`limit_reputation` int(11) DEFAULT NULL,
		} 
		'''
		return self.data(info).add()

