#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="scorpiotool",
    version="0.1.4",
    description="xlsx tool",
    long_description="xlsx tool",

    url="https://github.com/vekair/PypiProject.git",
    author="vekair",
    author_email="vekair@126.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["xlsxwriter", "hashlib", "redis", "gzip", "random"]
)
