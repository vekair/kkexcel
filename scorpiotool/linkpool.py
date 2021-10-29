# /usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021-10-29 10:50
# @Author: wei kai
# @File    : linkpool.py
# @Software: PyCharm
import redis


class RedisUtils(object):
    def __init__(self, HOST, POST, PASSWORD=None, MAX_CONNECTIONS=None):
        self.host = HOST
        self.port = POST
        self.password = PASSWORD
        self.max_connections = MAX_CONNECTIONS

    def build_pika(self, redis_db):
        rdp = redis.ConnectionPool(host=self.host, port=self.port, db=redis_db, password=self.password,
                                   max_connections=self.max_connections)
        return redis.StrictRedis(connection_pool=rdp)
