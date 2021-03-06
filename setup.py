#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""\
#######
LUTLINE
#######

Parse `argv` using a look-up table generated from your command-line interface specification.

*******
Install
*******

Install lutline from PyPI with:

    $ pip install lutline

***********
Development
***********

====
Test
====

Test lutline using:

    $ python -m tests

"""


import os.path
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()
execfile('lutline/version.py')


setup(
    name='lutline',
    version=__version__,
    description="Parse argv using a look-up table generated from your CLI specification.",
    long_description=__doc__,
    author="Filipe Funenga",
    author_email="fmafunenga@gmail.com",
    url="http://ffunenga.github.io/lutline",
    license='MIT',
    keywords='cli argv command-line interface arguments',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
    ],
    packages=['lutline', 'lutline.templates'],
    entry_points={
        'console_scripts': [
            'lutline = lutline.main:main',
        ],
    },
)
