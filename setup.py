#!/usr/bin/env python
# coding=utf8

"""
Copyright 2015 jenny
"""

from setuptools import setup, find_packages

setup(
    name='jenny',
    version='0.0.1',
    description='jenny Project',
    include_package_data=True,
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
)