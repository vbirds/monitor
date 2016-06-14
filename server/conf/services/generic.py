#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__='jhz'

class BasicService(object):
    def __init__(self):
        self.name = 'BasicService name'
        self.interval = 300
        self.plugin_name = 'your_plugin_name'
        self.triggers = {}