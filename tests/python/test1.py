#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools


def run():
    import lutline

    usage = "usage: (...)"
    spec = [
        ['exc', [
            [
                ['opt', [['f', 'l'],
                         ['a', 'language']]],
                ['opt', [['f', 'o'],
                         ['a', 'output_file']]],
                ['a', 'spec_file'],
            ],
            [
                ['c', 'dump'],
                ['a', 'spec_file']
            ]
        ]]
    ]

    embodiments = lutline.embodiments.process(spec)
    lutline.validate.process(embodiments)
    lut = lutline.lut.generate(embodiments)
    rst = lutline.templates.export(usage, lut, "python")
    with open("temp.py", "w") as f:
        f.write(rst)

    temp = importlib.import_module("temp", ".")
    reload(temp)
    count = 0
    rsts = []
    samples = ['-l', '--l', '-l1', 'python', '-o', '--o', '-o1', 'file.txt']
    for i in range(max(len(e) for e in embodiments) + 1):
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
    assert len(rsts) == 18
    assert ('python',) in rsts
    assert ('file.txt',) in rsts
    assert ('-l', 'python', 'python') in rsts
    assert ('-l', 'python', 'file.txt') in rsts
    assert ('-l', 'file.txt', 'python') in rsts
    assert ('-l', 'file.txt', 'file.txt') in rsts
    assert ('-o', 'python', 'python') in rsts
    assert ('-o', 'python', 'file.txt') in rsts
    assert ('-o', 'file.txt', 'python') in rsts
    assert ('-o', 'file.txt', 'file.txt') in rsts
    assert ('-l', 'python', '-o', 'python', 'python') in rsts
    assert ('-l', 'python', '-o', 'python', 'file.txt') in rsts
    assert ('-l', 'python', '-o', 'file.txt', 'python') in rsts
    assert ('-l', 'python', '-o', 'file.txt', 'file.txt') in rsts
    assert ('-l', 'file.txt', '-o', 'python', 'python') in rsts
    assert ('-l', 'file.txt', '-o', 'python', 'file.txt') in rsts
    assert ('-l', 'file.txt', '-o', 'file.txt', 'python') in rsts
    assert ('-l', 'file.txt', '-o', 'file.txt', 'file.txt') in rsts

    rsts = []
    samples = ['dump', 'dumps', 'file.txt', '-f']
    for i in range(max(len(e) for e in embodiments) + 1):
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
    assert len(rsts) == 6
    assert ('dump',) in rsts
    assert ('dumps',) in rsts
    assert ('file.txt',) in rsts
    assert ('dump', 'dump') in rsts
    assert ('dump', 'dumps') in rsts
    assert ('dump', 'file.txt') in rsts

    print "tested", count, "possibilities",
    os.remove("temp.py")
    os.remove("temp.pyc")
