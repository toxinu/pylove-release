#!/usr/bin/env python
# coding: utf-8
import os
import sys
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = []


def read_requirements():
    with open('requirements.txt') as r:
        for l in r.readlines():
            requirements.append(l)


def get_version():
    VERSIONFILE = 'love_release/__init__.py'
    initfile_lines = open(VERSIONFILE, 'rt').readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='love_release',
    version=get_version(),
    description='',
    long_description=open('README.rst').read(),
    license=open("LICENSE").read(),
    author="Geoffrey LEHEE",
    author_email="hello@socketubs.org",
    url='https://github.com/socketubs/love_release',
    keywords="",
    packages=['love_release'],
    scripts=['bin/love-release'],
    install_requires=read_requirements(),
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4']
)
