# /usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021-10-29 10:37
# @Author: wei kai
# @File    : utils.py
# @Software: PyCharm
import gzip
import random


def random_user_agent(self):
    """
    获取随机安卓UA
    :return:
    """
    a = random.randint(14, 30)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    os = '{}.{}.{}'.format(random.randint(15, 19), b, b)
    UA = "com.ss.android.ugc.aweme/{}0{}0{} (Linux; U; Android {}; zh_CN; Nexus 5; Build/QKQ1.190828.002; Cronet/TTNetVersion:{} 2020-04-03 QuicVersion:{} 2020-05-20)".format(
        a, b, c, os, self.stringRandom(8), self.stringRandom(8))
    return UA


def gzip_compress(buf):
    """
    gzip压缩
    :param buf:
    :return:
    """
    return gzip.compress(str(buf).encode())
