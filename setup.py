#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: liyanyi 
# Mail: lwl20080304@163com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "liyanyi_utils",
    version = "0.0.1",
    keywords = ("pip", "datacanvas", "eds", "liyanyi"),
    description = "eds sdk",
    long_description = "eds sdk for python",
    license = "MIT Licence",

    url = "http://liyanyi.com",
    author = "liyanyi",
    author_email = "lwl20080304@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
