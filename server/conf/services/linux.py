#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__= 'jhz'

from generic import BasicService

class CPU(BasicService):
    def __init__(self):
        super(CPU, self).__init__()
        self.interval = 30
        self.name = 'linux_cpu'
        self.plugin_name = 'get_cpu_status'

        self.triggers = {
            'idle':{
                'func':'avg',
                'last': 10*60,
                'operator': 'lt',
                'count': 1,
                'warning': 70,
                'critical': 75,
                'data_type': float
            },
            'iowait':{
                'func': 'hit',
                'last': 15 * 60,
                'count': 5,
                'operator': 'gt',
                'warning': 40,
                'critical': 50,
                'data_type': float
            }
        }

class Memory(BasicService):
    def __init__(self):
        super(Memory, self).__init__()
        self.interval = 20
        self.name = 'linux_mem'
        self.plugin_name = 'get_mem_status'

        self.triggers = {
            'MemUsage_p': {
                'func': 'avg',
                'last': 5 * 60,
                'count': 1,
                'operator': 'gt',
                'warning': 80,
                'critical': 90,
                'data_type': float
            }
        }

class Network(BasicService):
    def __init__(self):
        super(Network, self).__init__()
        self.interval =60
        self.name = 'linux_network'
        self.plugin_name = 'get_network_status'

        self.triggers = {
            'in': {
                'func': 'hit',
                'last': 10 * 60,
                'count': 5,
                'operator': 'gt',
                'warning': 1024 * 1024 * 10,
                'critical': 1024 * 1024 * 15,
                'data_type': float
            },
            'out': {
                'func': 'hit',
                'last': 10 * 60,
                'count': 5,
                'operator': 'gt',
                'warning': 1024 * 1024 * 10,
                'critical': 1024 * 1024 * 15,
                'data_type': float
            }
        }