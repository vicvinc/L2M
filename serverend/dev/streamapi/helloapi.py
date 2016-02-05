#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-10 10:04:04
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-10 10:04:09

import stream
client = stream.connect('wuu4zhjnj2k2', '8u8npqaamm8qr8pysumfrp9s5umc77yvvqyhkqsukm6drpmhm5xw5pbxbxwr9tbp')
# Get the feed object
eric_feed = client.feed('user', 'eric')
# Add the activity to the feed
eric_feed.add_activity({'actor': 'eric', 'verb': 'tweet', 'object': 1, 'tweet': 'Hello world'});