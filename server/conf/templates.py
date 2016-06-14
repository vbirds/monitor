#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'jhz'

from services import linux


class BaseTemplate(object):
    def __init__(self):
        self.name = 'you temlate name'
        self.hosts = []
        self.services = []

class LinuxGenericTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxGenericTemplate, self).__init__()
        self.name = 'LinuxCommonServices'
        self.services = [
            linux.CPU(),
            linux.Memory(),
        ]

        self.services[0].interval = 90

class LinuxSpecial(BaseTemplate):
    def __init__(self):
        super(LinuxSpecial, self).__init__()
        self.name = 'LinuxSpecialServices'
        self.services = [
            linux.CPU(),
            linux.Network()
        ]

