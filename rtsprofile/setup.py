#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rtsprofile'],
    package_dir={'': 'lib/python2.7/site-packages'}
)

setup(**d)
