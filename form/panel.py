#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vicvinc
# @Date:   2015-07-22 14:30:35
# @Last Modified by:   Administrator
# @Last Modified time: 2015-07-22 19:02:42

from wtforms import TextField, HiddenField, validators
from lib.forms import Form

class CreatePanel(Form):
	'''panel form validators'''
	#def __init__(self, arg):
	#	super(CreatePanel, self).__init__()
	#	self.arg = arg
	title = TextField('Title', [
		validators.Required(message = '请填写面板标题'),
		validators.Length(min = 2, message = '面板标题长度过短（2个字符）'),
		validators.Length(max = 8, message = '面板标题长度过长（8个字符）'),
	])
	content = TextField('Content', [
		validators.Required(message = '请填写面板描述'),
		validators.Length(min = 14, message = '面板内容长度过短（少于14个字符）'),
	])