#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'jhz'

import redishelper
import serialize
from conf import hosts
import json,time,threading


class MonitorServer(object):
    def __init__(self):
        self.r = redishelper.RedisHelper()
        self.r.set("name", 'jhz')
        self.save_configs()

    def save_configs(self):
        serialize.push_all_configs_into_redis(self, hosts.monitored_groups)

    def start(self):
        pass

    def handle(self):
        pass
