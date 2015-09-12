#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os



def run():
    import lutline

    usage = "usage: (...)"
    spec = [
        [u'exc', [
            [
                [u'opt', [[u'f', u'l'],
                          [u'a', u'language']]],
                [u'opt', [[u'f', u'o'],
                          [u'a', u'output_file']]],
                [u'a', u'spec_file'],
            ],
            [
                [u'c', u'dump'],
                [u'a', u'spec_file']
            ]
        ]]
    ]
    
    print    
    print "embodiments..."
    embodiments = lutline.embodiments.process(spec)
    print "validate..."
    lutline.validate.process(embodiments)
    print "lut..."
    lut = lutline.lut.generate(embodiments)
    print "templates.export..."
    rst = lutline.templates.export(spec, usage, lut, "python")
    with open("temp.py", "w") as f:
        f.write(rst)