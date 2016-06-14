#!/usr/bin/env python
#coding:utf-8

import load,cpu,memory


def get_network_status():
    return load.monitor()

def get_cpu_status():
    #return cpu.monitor()
    return cpu.monitor()

def get_mem_status():
    return memory.monitor()

if __name__ == '__main__':
  print get_cpu_status()