#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of tkintertools.
# https://github.com/Jovascript/TkinterTools

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Joe <joe.bell34@btinternet.com>

from setuptools import setup, find_packages
from tkintertools import __version__


setup(
    name='tkintertools',
    version=__version__,
    description='A set of useful helpers for developing tkinter applications.',
    long_description='''
A set of useful helpers for developing tkinter applications.
''',
    keywords='tkinter ease nootworthy',
    author='Joe',
    author_email='joe.bell34@btinternet.com',
    url='https://github.com/Jovascript/TkinterTools',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'tkintertools=tkintertools.cli:main',
        ],
    },
)
