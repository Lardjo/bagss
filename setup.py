#!usr/bin/env python3
# File: setup.py
# Setup file

import sys

from distutils.core import setup

sys.path.append('../')

import BAGSS

setup (name = "BAGSS", 
	version = BAGSS.__version__, 
	author = BAGSS.__author__, 
	py_modules = ["BAGSS"], 
	)