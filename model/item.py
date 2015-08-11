#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sguar
# @Date:   2015-08-01 22:56:50
# @Last Modified by:   Sguar
# @Last Modified time: 2015-08-02 06:07:34

import time
from lib.query import Query

class ItemModel(Query):
	def __init__(self, db):
		self.db = db
		self.table_name = "item"
		super(ItemModel, self).__init__()

	def get_all_items(self):
		return self.select()

	def add_new_item(self, info):
		return self.data(info).add()

	def get_item_by_itemid(self, itemid):
		where = "itemid = %s" % itemid
		return self.where(where).find()