#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vicvinc
# @Date:   2015-08-04 16:52:08
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-04 20:46:36

import uuid
import hashlib
import StringIO
import time
import json
import re
import urllib2
import urllib
import tornado.web
import lib.jsonp
import os

from pprint import pprint
from base import *
from lib.sendmail import send
from lib.variables import gen_random
from lib.gravatar import Gravatar
from form.user import *

def do_login(self, user_id):
	user_info = self.user_model.get_user_by_uid(user_id)
	user_id = user_info["uid"]
	self.session["uid"] = user_id
	self.session["username"] = user_info["username"]
	self.session["email"] = user_info["email"]
	self.session["password"] = user_info["password"]
	self.session.save()
	self.set_secure_cookie("user", str(user_id))

def do_logout(self):
	# destroy sessions
	self.session["uid"] = None
	self.session["username"] = None
	self.session["email"] = None
	self.session["password"] = None
	self.session.save()

	# destroy cookies
	self.clear_cookie("user")

class HomeHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		user_email = self.current_user['email']
		self.write(user_email)

class SettingHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self, tv = {}):
		user_info = self.get_current_user()
		tv["user_info"] = user_info
		tv["gen_random"] = gen_random
		self.render("user/setting.html", **tv)

	@tornado.web.authenticated
	def post(self, tv = {}):
		tv = {}

		# validate the fields

		form = SettingForm(self)

		if not form.validate():
			resp_msg = {
				'code': 1, # 1 success , 0 faied 
				'data': '', # db handler result
				'msg': form.errors # http handler result
			}
			self.finish(resp_msg)
			return

		user_info = self.current_user
		update_result = self.user_model.set_user_base_info_by_uid(user_info["uid"], {
			"nickname": form.nickname.data,
			"signature": form.signature.data,
			"location": form.location.data,
			# "website": form.website.data,
			# "inventory": form.inventory.data,
			"fvteam": form.fvteam.data,
			"weibo": form.weibo.data,
			"steamid": form.steamid.data,
			"self_intro": form.self_intro.data,
		})

		updated = self.user_model.set_user_base_info_by_uid(user_info["uid"], {"updated": time.strftime('%Y-%m-%d %H:%M:%S')})
		self.set_status(200, 'save avatar succeed')
		resp_msg = {
			'code': 1, # 1 success , 0 faied 
			'data': update_result, # db handler result
			'msg': '用户基本资料更新成功' # http handler result
		}
		self.finish(resp_msg)

class SettingAvatarHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self, tv = {}):
		user_info = self.get_current_user()
		tv["user_info"] = user_info
		tv["gen_random"] = gen_random
		self.render("user/setting_avatar.html", **tv)

	@tornado.web.authenticated
	def post(self, tv = {}):
		tv = {}
		# post_data = json.loads(self.request.body)
		post_data = self.request.body
		avatar = self.get_body_argument('avatar')
		#what will happend if avatar is none? 400 error happends redefine this error handler

		user_info = self.current_user

		user_id = user_info["uid"]
		avatar_name = avatar
		
		result = self.user_model.set_user_avatar_by_uid(user_id, avatar_name)
		#what if update db failed curse? error return need to be re defined 
		updated = self.user_model.set_user_base_info_by_uid(user_id, {"updated": time.strftime('%Y-%m-%d %H:%M:%S')})
		self.set_status(200, 'save avatar succeed')
		resp_msg = {
			'code': 1, # 1 success , 0 faied 
			'data': result, # db handler result
			'msg': '用户头像更新成功' # http handler result
		}
		# self.write(resp_msg)
		self.finish(resp_msg)
		# update `updated`

class SettingPasswordHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self, tv = {}):
		user_info = self.get_current_user()
		tv["user_info"] = user_info
		tv["gen_random"] = gen_random
		self.render("user/setting_password.html", **tv)

	@tornado.web.authenticated
	def post(self, tv = {}):
		tv = {}

		# validate the fields

		form = SettingPasswordForm(self)

		if not form.validate():
			self.get({"errors": form.errors})
			return

		# validate the password

		user_info = self.current_user
		user_id = user_info["uid"]
		secure_password = hashlib.sha1(form.password_old.data).hexdigest()
		secure_new_password = hashlib.sha1(form.password.data).hexdigest()

		if(not user_info["password"] == secure_password):
			tv["errors"] = {}
			tv["errors"]["error_password"] = [u"当前密码输入有误"]
			self.get(tv)
			return

		# continue while validate succeed

		update_result = self.user_model.set_user_password_by_uid(user_id, secure_new_password)
		tv["success_message"] = [u"您的用户密码已更新"]
		# update `updated`
		updated = self.user_model.set_user_base_info_by_uid(user_id, {"updated": time.strftime('%Y-%m-%d %H:%M:%S')})
		self.get(tv)

class ForgotPasswordHandler(BaseHandler):
	def get(self, tv = {}):
		do_logout(self)
		self.render("user/forgot_password.html", **tv)

	def post(self, tv = {}):
		tv = {}

		# validate the fields

		form = ForgotPasswordForm(self)

		if not form.validate():
			self.get({"errors": form.errors})
			return
		# validate the post value

		user_info = self.user_model.get_user_by_email_and_username(form.email.data, form.username.data)

		if(not user_info):
			tv["errors"] = {}
			tv["errors"]["invalid_email_or_username"] = [u"所填用户名和邮箱有误"]
			self.get(tv)
			return

		# continue while validate succeed
		# update password
		new_password = uuid.uuid1().hex
		new_secure_password = hashlib.sha1(new_password).hexdigest()
		update_result = self.user_model.set_user_password_by_uid(user_info["uid"], new_secure_password)

		# send password reset link to user

		mail_title = u"D2Ark社区（D2Ark.com）找回密码"
		tv = {"email": form.email.data, "new_password": new_password};
		tv["success_message"] = [u"新密码已发送至您的注册邮箱"]
		mail_content = self.render_string("user/forgot_password_mail.html", **tv)
		send(mail_title, mail_content, form.email.data)

		self.get(tv)

class LoginHandler(BaseHandler):
	def get(self, tv = {}):
		do_logout(self)
		self.render("user/login.html", **tv)

	def post(self, tv = {}):
		tv = {}

		# validate the fields

		form = LoginForm(self)

		if not form.validate():
			self.get({"errors": form.errors})
			return

		# continue while validate succeed
		
		secure_password = hashlib.sha1(form.password.data).hexdigest()
		secure_password_md5 = hashlib.md5(form.password.data).hexdigest()
		user_info = self.user_model.get_user_by_email_and_password(form.email.data, secure_password)
		user_info = user_info or self.user_model.get_user_by_email_and_password(form.email.data, secure_password_md5)
		
		if(user_info):
			do_login(self, user_info["uid"])
			# update `last_login`
			updated = self.user_model.set_user_base_info_by_uid(user_info["uid"], {"last_login": time.strftime('%Y-%m-%d %H:%M:%S')})
			self.redirect(self.get_argument("next", "/"))
			return

		tv["errors"] = {"invalid_email_or_password": [u"邮箱或者密码不正确"]}
		self.get(tv)

class LogoutHandler(BaseHandler):
	def get(self):
		do_logout(self)
		# redirect
		self.redirect(self.get_argument("next", "/"))

class RegisterHandler(BaseHandler):
	def get(self, tv = {}):
		do_logout(self)
		self.render("user/register.html", **tv)

	def post(self, tv = {}):
		tv = {}

		# validate the fields

		form = RegisterForm(self)

		if not form.validate():
			self.get({"errors": form.errors})
			return

		# validate duplicated

		duplicated_email = self.user_model.get_user_by_email(form.email.data)
		duplicated_username = self.user_model.get_user_by_username(form.username.data)

		if(duplicated_email or duplicated_username):
			tv["errors"] = {}

			if(duplicated_email):
				tv["errors"]["duplicated_email"] = [u"所填邮箱已经被注册过"]

			if(duplicated_username):
				tv["errors"]["duplicated_username"] = [u"所填用户名已经被注册过"]

			self.get(tv)
			return

		# validate reserved

		if(form.username.data in self.settings.get("reserved")):
			tv["errors"] = {}
			tv["errors"]["reserved_username"] = [u"用户名被保留不可用"]
			self.get(tv)
			return

		# continue while validate succeed

		secure_password = hashlib.sha1(form.password.data).hexdigest()

		user_info = {
			"email": form.email.data,
			"password": secure_password,
			"username": form.username.data,
			"created": time.strftime('%Y-%m-%d %H:%M:%S')
		}

		if(self.current_user):
			return
		
		user_id = self.user_model.add_new_user(user_info)
		
		if(user_id):
			inv_info = {
				'uid': user_id
			}
			self.inventory_model.add_new_inventory(inv_info)

			do_login(self, user_id)

			mail_title = u"D2Ark社区（D2Ark.com）注册成功通知"
			mail_content = self.render_string("user/register_mail.html")
			send(mail_title, mail_content, form.email.data)
		self.redirect(self.get_argument("next", "/"))

class ItemShopHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self, tv = {}):
		user_info = self.get_current_user()
		user_item_list = get_user_inv_list(self, user_info['uid'])
		tv["user_info"] = user_info
		tv['user_inv_list'] = user_item_list
		tv["gen_random"] = gen_random
		self.render("grade/itemshop.html", **tv)

	@tornado.web.authenticated
	def post(self, tv = {}):
		tv = {}
		user_info = self.current_user
		form = SettingForm(self)
		if not form.validate():
			data = {
				'success': 0, # 1 success , 0 faied 
				'error': form.errors,
				'msg': 'err msg', 
			}
			self.finish(resp_msg)
			return

		action = self.get_argument('action').encode('utf-8')
		if( action == 'filter' ):
			available_slots = get_user_available_slots(self, user_info['uid'])
			data = {
				'items' : self.item_model.get_all_items(),
				'login_status' : True,
				'available_slots': available_slots,
				'available_gold': user_info['gold']
			}
			self.write(data)

		if( action == 'buy_item' ):
			item_id = self.get_argument('item_id')
			item_info = self.item_model.get_item_by_itemid(item_id)
			user_gold = int(user_info['gold'])
			cost = int(item_info['cost'])

			if(user_gold < cost):
				data = {
					'success': 0, # 1 success , 0 faied 
					'user_inv_list': [],
					'available_gold': user_gold_update,
					'error': '金币不足'
				}
			else:
				user_gold_update = user_gold - cost
				user_info_update = {
					'gold' : user_gold_update
				}
				user_inv = self.inventory_model.get_inventory_by_user_id(int(user_info['uid']))

				if( not user_inv['inv1'] ):
					inventory_info_update = {
						'inv1': item_id
					}
				elif( not user_inv['inv2'] ):
					inventory_info_update = {
						'inv2': item_id
					}
				elif( not user_inv['inv3'] ):
					inventory_info_update = {
						'inv3': item_id
					}
				elif( not user_inv['inv4'] ):
					inventory_info_update = {
						'inv4': item_id
					}
				elif( not user_inv['inv5'] ):
					inventory_info_update = {
						'inv5': item_id
					}
				elif( not user_inv['inv6'] ):
					inventory_info_update = {
						'inv6': item_id
					}

				inv_update_result = self.inventory_model.set_inventory_by_uid(int(user_info['uid']), inventory_info_update)
				user_update_result = self.user_model.set_user_base_info_by_uid(int(user_info['uid']), user_info_update)
				#db return: 0 success 1 faild

				if( inv_update_result or user_update_result ):
					#failed
					data = {
						'success': 0, # 1 success , 0 faied 
						'user_inv_list': [],
						'available_gold': user_gold_update,
						'error': inv_update_result + inv_update_result
					}
				else:
					#success
					new_user_inv_list = get_user_inv_list(self, user_info['uid'])
					data = {
						'success': 1, # 1 success , 0 faied 
						'user_inv_list': new_user_inv_list,
						'available_gold': user_gold_update
					}
					
			self.write(data)

		if( action == 'sell_item' ):
			item_id = self.get_argument('item_id')
			slot = self.get_argument('slot')
			item_info = self.item_model.get_item_by_itemid(item_id)
			user_gold = int(user_info['gold'])
			cost = int(item_info['cost'])
			user_gold_update = user_gold + cost
			user_info_update = {
				'gold' : user_gold_update
			}
			inventory_info_update = {
				'inv'+slot: ''
			}

			user_update_result = self.user_model.set_user_base_info_by_uid(int(user_info['uid']), user_info_update)
			inv_update_result = self.inventory_model.set_inventory_by_uid(int(user_info['uid']), inventory_info_update)

			if( inv_update_result or user_update_result ):
				#failed
				data = {
					'success': 0, # 1 success , 0 faied 
					'user_inv_list': [],
					'available_gold': user_gold_update,
					'error': inv_update_result + inv_update_result
				}
			else:
				#success
				new_user_inv_list = get_user_inv_list(self, user_info['uid'])
				data = {
					'success': 1, # 1 success , 0 faied 
					'user_inv_list': new_user_inv_list,
					'available_gold': user_gold_update
				}
			self.write(data)

		self.finish()

def get_user_inv_list(self, uid):
	user_inv_data = self.inventory_model.get_inventory_by_user_id(int(uid))
	#for users dont have inventory data
	if user_inv_data is None:
		inv_info = {
			'uid': int(uid)
		}
		user_info = {
			'gold': 625
		}
		self.user_model.set_user_base_info_by_uid(int(uid), user_info)
		self.inventory_model.add_new_inventory(inv_info)
		user_inv_data = self.inventory_model.get_inventory_by_user_id(int(uid))
	#
	user_item_list = []
	for x in user_inv_data:
		if ( x=='id' or x=='uid'):
			continue
		elif( x=='inv1' ):
			if(user_inv_data[x]):
				uinv_info = self.item_model.get_item_by_itemid(user_inv_data[x])
				uinv_info['slot'] = 1
			else:
				uinv_info = None
		elif( x=='inv2' ):
			if(user_inv_data[x]):
				uinv_info = self.item_model.get_item_by_itemid(user_inv_data[x])
				uinv_info['slot'] = 2
			else:
				uinv_info = None
		elif( x=='inv3' ):
			if(user_inv_data[x]):
				uinv_info = self.item_model.get_item_by_itemid(user_inv_data[x])
				uinv_info['slot'] = 3
			else:
				uinv_info = None
		elif( x=='inv4' ):
			if(user_inv_data[x]):
				uinv_info = self.item_model.get_item_by_itemid(user_inv_data[x])
				uinv_info['slot'] = 4
			else:
				uinv_info = None
		elif( x=='inv5' ):
			if(user_inv_data[x]):
				uinv_info = self.item_model.get_item_by_itemid(user_inv_data[x])
				uinv_info['slot'] = 5
			else:
				uinv_info = None
		elif( x=='inv6' ):
			if(user_inv_data[x]):
				uinv_info = self.item_model.get_item_by_itemid(user_inv_data[x])
				uinv_info['slot'] = 6
			else:
				uinv_info = None
		user_item_list.insert(0, uinv_info)
	return user_item_list

def get_user_available_slots(self, uid):
	user_inv = self.inventory_model.get_inventory_by_user_id(int(uid))
	available_slots = 6
	for x in user_inv:
		if (x=='id' or x == 'uid'):
			continue
		elif( user_inv[x] ):
			available_slots-=1
	return available_slots