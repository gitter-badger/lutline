#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import lutline


def run():
    # ./app [<fout>] [<fin>]
    spec = [
        [u'opt', [[u'a', u'fout']]],
        [u'opt', [[u'a', u'fin']]],
    ]
    embodiments = lutline.embodiments.process(spec)
    try:
        lutline.validate.process(embodiments)
    except SystemExit as e:
        pass
    else:
        raise Exception("test failed")
