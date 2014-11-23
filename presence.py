#!/bin/python

# NOTE: if run in docker, docker must be run with net=host !!!

import sys
import etcd
import netifaces
import signal
from time import sleep

client = etcd.Client()

def dereg_func():
    def handler(*args, **kwargs):
        client.delete('/db/addr')
        sys.exit(0)
    return handler

deregister = dereg_func()
signal.signal(signal.SIGTERM, deregister)
signal.signal(signal.SIGINT, deregister)

while True:
    ip = netifaces.ifaddresses(
        netifaces.gateways()['default'][netifaces.AF_INET][1]
    )[netifaces.AF_INET][0]['addr']

    client.write('/db/addr', ip, ttl=30)
    sleep(10)
