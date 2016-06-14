#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'jhz'

from conf import hosts
import json,time,operator

def push_all_configs_into_redis(main_ins,host_groups):
    host_config_dic = {}

    for group in host_groups:
        # 循环主机里的机器
        for host in group.hosts:
            # 给每台主机生成配置字典
            if host not in host_config_dic:
                host_config_dic[host] = {}

            # 循环服务组里要循环的服务
            for s in group.services:
                host_config_dic[host][s.name] = [
                    s.plugin_name,
                    s.interval
                ]

    for h, v in host_config_dic.items():
        #print h, v
        host_config_key = "HostConfig::%s" %h
        main_ins.r.set(host_config_key, json.dumps(v))

def fetch_all_config(host_groups):
    host_config_dic = {}

    for group in host_groups:
        # 循环主机里的机器
        for host in group.hosts:
            # 给每台主机生成配置字典
            if host not in host_config_dic:
                host_config_dic[host] = {}

            # 循环服务组里要循环的服务
            for s in group.services:
                host_config_dic[host][s.name] = s

    for h,v in host_config_dic.items():
        print h ,v
    return host_config_dic


