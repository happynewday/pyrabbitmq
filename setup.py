#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pyrabbitmq',
        version = '1.0',
        install_requires = [
                'pika', 
                'pybase @ git+https://github.com/happynewday/pybase.git@master'], 
        description = 'rabbitmq consumer, publisher',
        url = 'https://github.com/happynewday/pyrabbitmq', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.8',],
        packages = ['pyrabbitmq'],
        data_files = [ ],  
        entry_points = { }   
        )
