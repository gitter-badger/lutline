#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools
import lutline


def run():
    usage = """\
usage: lutline [-l <language>] [-o <output_file>] <spec_file>
       lutline dump <spec_file>

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
    embodiments = lutline.embodiments.process(spec)
    lutline.validate.process(embodiments)
    lut = lutline.lut.generate(embodiments)
    rst = lutline.format.export(usage, lut, "py")
    with open("temp2.py", "w") as f:
        f.write(rst)
    temp = importlib.import_module("temp2", ".")

    count = 0
    rsts = []
    samples = ['file.txt_py', '-f', '-f1', '-o', '-o1', '-l', '-l1', '-a']
    for i in range(max(len(e) for e in embodiments)):
        iterator = [] if i == 0 else itertools.product(samples, repeat=(i + 1))
        for op in iterator:
            count += 1
            try:
                rst = temp.parse(op)
                assert type(rst) == dict
            except KeyboardInterrupt:
                return
            except SystemExit:
                pass
            else:
                rsts.append(op)
    samples = ['dump', 'dumps', 'file.txt_py', '-f', '-f1', '--f', '-a']
    for i in range(max(len(e) for e in embodiments)):
        iterator = [] if i == 0 else itertools.product(samples, repeat=(i + 1))
        for op in iterator:
            count += 1
            try:
                rst = temp.parse(op)
                assert type(rst) == dict
            except KeyboardInterrupt:
                return
            except SystemExit:
                pass
            else:
                rsts.append(op)
    aims = [('-o', 'file.txt_py', 'file.txt_py'),
            ('-l', 'file.txt_py', 'file.txt_py'),
            ('-l', 'file.txt_py', '-o', 'file.txt_py', 'file.txt_py'),
            ('dump', 'dump'),
            ('dump', 'dumps'),
            ('dump', 'file.txt_py')]
    assert len(rsts) == len(aims)
    for aim in aims:
        assert aim in rsts
    print "tested", count, "possibilities",
    os.remove("temp2.py")
    os.remove("temp2.pyc")
