#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="kkexcel",
    version="0.1.8",
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

"""
打包上传
python3 setup.py sdist

twine upload dist/*

python -m pip install kkexcel --upgrade -i https://pypi.org/simple   # 及时的方式，不用等待 阿里云 豆瓣 同步


"""