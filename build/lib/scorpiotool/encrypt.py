# /usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021-10-29 10:25
# @Author: wei kai
# @File    : encrypt.py
# @Software: PyCharm
import hashlib


def md5Saam(data):
    """
    md5
    :return:
    """
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()


