#!/usr/bin/env python
#-*- coding:utf-8 -*-


import lutline


def run():
    # ./app [-f] <fin>
    spec = [
        [u'opt', [[u'f', u'f'], [u'a', u'fout']]],
        [u'a', u'fin']
    ]
    embodiments = lutline.all_embodiments(spec)
    lutline.validate_embodiments(embodiments)
    lut = lutline.generate_lut(embodiments)
    print(lutline.export("./app [-f <fout>] <fin>", lut, "python"))
