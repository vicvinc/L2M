#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sguar
# @Date:   2015-08-01 23:52:23
# @Last Modified by:   Sguar
# @Last Modified time: 2015-08-02 06:07:56

import time
from lib.query import Query

class InventoryModel(Query):
	def __init__(self, db):
		self.db = db
		self.table_name = "inventory"
		super(InventoryModel, self).__init__()

	def add_new_inventory(self, info):
		return self.data(info).add()

	def get_inventory_by_user_id(self, uid):
		where = "uid = %s" % uid
		return self.where(where).find()

	def set_inventory_by_uid(self, uid, info):
		where = "uid = %s" % uid
		return self.data(info).where(where).save()