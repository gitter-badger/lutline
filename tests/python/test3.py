#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools


def run():
    import lutline

    usage = ("Usage:\n"
             "    ./hotel {-q (-v | -v1 | -v2)} <rooms>\n"
             "    ./hotel -v [<request>]\n")

    spec = [
        ['exc', [
            [
                ['uns', [
                    [['f', 'q']],
                    [['exc', [
                        [['f', 'v']],
                        [['f', 'v1']],
                        [['f', 'v2']],
                    ]]
                    ]
                ]],
                ['a', 'rooms'],
            ],
            [
                ['f', 'v'],
                ['opt', [
                    ['a', 'request']]
                ]
            ]
        ]]
    ]

    embodiments = lutline.embodiments.process(spec)
    lutline.validate.process(embodiments)
    lut = lutline.lut.generate(embodiments)
    rst = lutline.templates.export(spec, usage, lut, "python")
    with open("temp.py", "w") as f:
        f.write(rst)

    temp = importlib.import_module("temp", ".")
    reload(temp)
    count = 0
    rsts = []
    samples = ['-v', '--v', '-v1', 'rooms.txt']
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

    assert len(rsts) == 2
    assert ('-v',) in rsts
    assert ('-v', 'rooms.txt') in rsts

    rsts = []
    samples = ['-q', '-v', '-v1', '-v2', '--v', 'rooms.txt']
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

    assert len(rsts) == 8
    assert ('-v',) in rsts
    assert ('-v', 'rooms.txt') in rsts
    assert ('-q', '-v', 'rooms.txt') in rsts
    assert ('-q', '-v1', 'rooms.txt') in rsts
    assert ('-q', '-v2', 'rooms.txt') in rsts
    assert ('-v', '-q', 'rooms.txt') in rsts
    assert ('-v1', '-q', 'rooms.txt') in rsts
    assert ('-v2', '-q', 'rooms.txt') in rsts

    print "tested", count, "possibilities",
    os.remove("temp.py")
    os.remove("temp.pyc")
