#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools


def run():
    import lutline

    usage = "usage: ./app [-f <fout>] <fin>"
    spec = [
        ['opt', [['f', 'f'],
                 ['a', 'fout']]],
        ['a', 'fin']
    ]

    embodiments = lutline.embodiments.process(spec)
    assert len(embodiments) == 2
    lutline.validate.process(embodiments)
    lut = lutline.lut.generate(embodiments)
    rst = lutline.templates.export(spec, usage, lut, "python")
    with open("temp.py", "w") as f:
        f.write(rst)

    temp = importlib.import_module("temp", ".")
    reload(temp)
    count = 0
    rsts = []
    samples = ['file.txt', '-file.txt', '-f', '-f1', '-ff', '--f',
               '-a']
    for i in range(max(len(e) for e in embodiments) + 2):
        iterator = itertools.product(samples, repeat=i)
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
    assert len(rsts) == 2
    assert ('file.txt',) in rsts
    assert ('-f', 'file.txt', 'file.txt') in rsts
    print "tested", count, "possibilities",
    os.remove("temp.py")
    os.remove("temp.pyc")
