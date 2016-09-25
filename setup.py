#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(name='data2args',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['pyyaml', 'six'])
