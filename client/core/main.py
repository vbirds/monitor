#_*_coding:utf-8_*_
__author__ = 'alex'

import sys
sys.path.append("..")

import json
import redishelper
from conf import settings
import time
import threading
from plugins import plugin_api

class MonitorClient(object):
    def __init__(self):
        self.r = redishelper.RedisHelper()
        self.ip = settings.ClientIP
        self.host_config = self.get_host_config()
    def start(self):
        self.handle()

    def get_host_config(self):
        config_key = "HostConfig::%s" % self.ip
        config = self.r.get(config_key)
        if config:
            config = json.loads(config)

        return config

    def handle(self):

        if self.host_config:
            while True:
                for service,val in self.host_config.items():
                    #print service,val
                    if len(val) <3: #确保第一次客户段启动时 会运行所有插件
                        self.host_config[service].append(0)

                    plugin_name , interval,last_run_time  = val  #last_run_time = 0
                    if time.time() - last_run_time < interval: # not reached the next run yet
                        next_run_time = interval - ( time.time() - last_run_time )
                        print "Service [%s] next run time is in [%s] secs" %(service, next_run_time)
                    else :
                        print "\033[32;1mgoing to run the [%s] again!\033[0m" % service
                        self.host_config[service][2] = time.time()
                        t = threading.Thread(target=self.call_plugin, args=(service, plugin_name))
                        t.start()

                time.sleep(1)

        else:
            print "\033[31;1mCannot get host config\033[0m"


    def call_plugin(self, service_name, plugin_name):
        func = getattr(plugin_api, plugin_name)

        service_data = func()
        print service_data
        report_data = {
            'host': self.ip,
            'service': service_name,
            'data': service_data
        }

        self.r.public(json.dumps(report_data))

        # print 'service [%s] res: %s' %(service_name,service_data)


