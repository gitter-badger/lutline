#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import lutline


def run():
    # ./app [<fout>] [<fin>]
    spec = [
        [u'opt', [[u'f', u'l'], [u'a', u'language']]],
    ]
    embodiments = lutline.embodiments.process(spec)
    lutline.validate.process(embodiments)
    print "embodiments:"
    for e in embodiments:
        print "   ", e
    lut = lutline.lut.generate(embodiments)
    print "lut:"
    for row in lut:
        print "   ", row
    rst = lutline.format.export("./app [-f <fout>] <fin>", lut, "py")
