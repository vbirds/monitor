#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'jhz'

import templates

#主机组一
web_clusters = templates.LinuxGenericTemplate()
web_clusters.hosts = [
    '10.225.100.65',
    '10.225.100.45',
    '10.225.100.51'
]

#主机组二
mysql_group = templates.LinuxSpecial()
mysql_group.hosts = [
    '10.225.100.65',
    '10.225.100.45',
    '10.225.100.72'
]

monitored_groups = [web_clusters, mysql_group]

if __name__ == '__main__':

    host_config_dic = {}

    for group in monitored_groups:
        #循环主机里的机器
        for host in group.hosts:
            #给每台主机生成配置字典
            if host not in host_config_dic:
                host_config_dic[host] = {}

            #循环服务组里要循环的服务
            for s in group.services:
                host_config_dic[host][s.name] = {
                    s.plugin_name,
                    s.interval
                }

    for h,v in host_config_dic.items():
        print h,v