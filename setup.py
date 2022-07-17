#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="kkexcel",
    version="0.1.6",
    description="json生成excel工具",
    long_description="json生成excel工具",

    url="https://github.com/vekair/kkexcel.git",
    author="vekair",
    author_email="vekair@126.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["xlsxwriter"]
)
