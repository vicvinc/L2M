#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vicvinc
# @Date:   2015-07-20 11:23:36
# @Last Modified by:   Administrator
# @Last Modified time: 2015-07-22 15:30:30

import time
from lib.query import Query

class PanelModel(Query):
	def __init__(self, db):
		self.db = db
		self.table_name = 'panel'
		super(PanelModel, self).__init__()
	def get_all_panels(self):
		return self.select()
	def get_all_panels_with_nodes(self):
		panels = self.get_all_panels()
		for panel in panels:
			where = 'panel_id = %s' % panel['id']
			panel['nodes'] = self.table('node').where(where).select()
		return panels
	def get_panel_by_panel_id(self):
		where = ''
		panels = self.get_all_panels()
		for panel in panels:
			where = 'panel_id = %s' % panel['id']
			panel['nodes'] = self.table('node').where(where).select()
		return panels
	def get_panel_by_panel_name(self):
		where = ''
		panels = self.get_all_panels()
		for panel in panels:
			where = 'panem_name = %s' % panel['name']
			panel['panel'] = self.table('panel').where(where).select()
		return panels
	def get_panel_by_user_last_created(self, uname):
		where = 'panel.owner = %s' % uname
		order = 'panel.created DESC'
		return self.where(where).order(order).find()
	def add_new_panel(self, p_info):
		return self.data(p_info).add()