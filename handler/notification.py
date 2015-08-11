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
import urllib2
import tornado.web
import lib.jsonp
import pprint

from base import *
from lib.variables import *
from form.topic import *
from lib.variables import gen_random
from lib.xss import XssCleaner
from lib.utils import find_mentions

class ListHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, tv = {}):
        #tv = template_variable
        user_info = self.current_user
        page = int(self.get_argument("p", "1"))
        tv["user_info"] = user_info
        tv["user_info"]["counter"] = {
            "topics": self.topic_model.get_user_all_topics_count(user_info["uid"]),
            "replies": self.reply_model.get_user_all_replies_count(user_info["uid"]),
            "favorites": self.favorite_model.get_user_favorite_count(user_info["uid"]),
        }

        tv["notifications_count"] = self.notification_model.get_user_unread_notification_count(user_info["uid"]);
        tv["notifications"] = self.notification_model.get_user_all_notifications(user_info["uid"], current_page = page)
        tv["active_page"] = "topic"
        tv["gen_random"] = gen_random

        # mark user unread notifications as read
        self.notification_model.mark_user_unread_notification_as_read(user_info["uid"])

        self.render("notification/notifications.html", **tv)

