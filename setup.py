#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

import data2args

setup(name='data2args',
      version=data2args.__version__,
      description='Create argument parsers from data structures.',
      long_description='Create argument parsers from data structures.',
      author='Gauvain Pocentek',
      author_email='gauvain@pocentek.net',
      license='LGPLv3',
      url='https://github.com/gpocentek/data2args',
      packages=find_packages(),
      install_requires=['cerberus', 'pyyaml', 'six'])
