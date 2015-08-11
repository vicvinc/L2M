#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 17:13:45
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-11 17:20:09

route = [
			(r"/", handler.index.HomeHandler),
			(r"/t/(\d+)", handler.topic.ViewHandler),
			(r"/t/create/(.*)", handler.topic.CreateHandler),
			(r"/t/edit/(.*)", handler.topic.EditHandler),
			(r"/reply/edit/(.*)", handler.topic.ReplyEditHandler),
			# change 'node' route handler form topic to node handler
			# (r"/node/(.*)", handler.topic.NodeTopicsHandler),
			(r'/node', handler.node.HomeHandler),
			(r"/node/(.*)", handler.node.NodeTopicsHandler),
			#add panel route
			(r'/panel', handler.panel.PanelHandler),
			#(r'/p/(.*)/topics', handler.panel.PanelTopicsHandler),
			#end panel route
			(r"/u/(.*)/topics", handler.topic.UserTopicsHandler),
			(r"/u/(.*)/replies", handler.topic.UserRepliesHandler),
			(r"/u/(.*)/favorites", handler.topic.UserFavoritesHandler),
			(r"/u/(.*)", handler.topic.ProfileHandler),

			(r"/vote", handler.topic.VoteHandler),
			(r"/favorite", handler.topic.FavoriteHandler),
			(r"/unfavorite", handler.topic.CancelFavoriteHandler),
			(r"/notifications", handler.notification.ListHandler),
			(r"/members", handler.topic.MembersHandler),
			(r"/setting", handler.user.SettingHandler),
			(r"/setting/avatar", handler.user.SettingAvatarHandler),
			(r"/setting/password", handler.user.SettingPasswordHandler),
			(r"/forgot", handler.user.ForgotPasswordHandler),
			(r"/login", handler.user.LoginHandler),
			(r"/logout", handler.user.LogoutHandler),
			(r"/register", handler.user.RegisterHandler),
			#add user item shop route
			(r"/itemshop", handler.user.ItemShopHandler),
			#end add 
			(r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
			(r"/static/avatar/(.*)", tornado.web.StaticFileHandler, dict(path = settings["avatar_path"])),
			(r"/(sitemap.*$)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
			(r"/(bdsitemap\.txt)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
			(r"/(.*)", handler.topic.ProfileHandler),
		]