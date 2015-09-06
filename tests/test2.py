#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools
import lutline


def run():
    usage = """\
usage: lutline [-l <language>] -f <spec_file> [-o <output_file>]
       lutline dump -f <spec_file>

Paramaters:
    -l <language>     Sets the output programming language. Default is 'py'.
    -f <spec_file>    Sets the input file with the specification.
    -o <output_file>  Sets the name of the output file to dump the parser code.
                      Default is 'cli.py'.
"""
    spec = [
        [u'exc', [
            [
                [u'opt', [[u'f', u'l'],
                          [u'a', u'language']]],
                [u'f', u'f'],
                [u'a', u'spec_file'],
                [u'opt', [[u'f', u'o'],
                          [u'a', u'output_file']]]
            ],
            [
                [u'c', u'dump'],
                [u'f', u'f'],
                [u'a', u'spec_file']
            ]
        ]]
    ]
    embodiments = lutline.embodiments.process(spec)
    lutline.validate.process(embodiments)
    lut = lutline.lut.generate(embodiments)
    rst = lutline.format.export(usage, lut, "py")
    with open("temp2.py", "w") as f:
        f.write(rst)
    return
    temp = importlib.import_module("temp2", ".")

    rsts = []
    samples = ['dump', 'dumps', 'file.txt_py', '-f', '-f1', '--f', '-o',
               '-o1', '--o', '-l', '-l1', '--l', '-a']
    for i in range(max(len(e) for e in embodiments) - 1):
        iterator = [] if i == 0 else itertools.product(samples, repeat=(i + 1))
        for op in iterator:
            try:
                rst = temp.parse(op)
                assert type(rst) == dict
            except KeyboardInterrupt:
                return
            except SystemExit:
                pass
            else:
                rsts.append(op)

    print "rsts:"
    for r in rsts:
        print " ", r
    print "---"
    os.remove("temp2.py")
    os.remove("temp2.pyc")
