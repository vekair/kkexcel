#!/usr/bin/env python
#-*- coding:utf-8 -*-



from setuptools import setup, find_packages

setup(
  name = "scorpiotool",
  version = "0.1.0",
  description = "xlsx tool",
  long_description = "xlsx tool",
  license = "MIT Licence",

  url = "https://github.com/wgq0335/scorpio.git",
  author = "justinwei",
  author_email = "wgq0335@163.com",

  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = ["xlsxwriter"]
)
