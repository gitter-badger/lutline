#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools


def run():
    import lutline

    usage = ("Usage:\n"
             "    ./kitchen burger [--raw | --medium | --overcooked]\n"
             "    ./kitchen [-u <urgency>] <request>\n"
             "    ./kitchen -h | --help | --version\n")

    spec = [
        ['exc', [
            [
                ['c', 'burger'],
                ['opt', [
                    ['exc', [
                        [['f', '-raw']],
                        [['f', '-medium']],
                        [['f', '-overcooked']]
                    ]]
                ]]
            ],
            [
                ['opt', [
                    ['f', 'u'],
                    ['a', 'urgency']]
                ],
                ['a', 'request']
            ],
            [
                ['exc', [
                    [['f', 'h']],
                    [['f', '-help']],
                    [['f', '-version']]
                ]]
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
    samples = ['burger', '--raw', '-raws', '--medium', '-meds',
               '--overcooked', '-overc']
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

    assert len(rsts) == 4
    assert ('burger',) in rsts
    assert ('burger', '--raw') in rsts
    assert ('burger', '--medium') in rsts
    assert ('burger', '--overcooked') in rsts

    rsts = []
    samples = ['-u', '--u', '-u1', 'request.txt', 'urgency',
               '--version', '-v', '--help', '-h', '--h', '-help']
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

    assert len(rsts) == 9
    assert ('request.txt',) in rsts
    assert ('urgency',) in rsts
    assert ('--version',) in rsts
    assert ('--help',) in rsts
    assert ('-h',) in rsts
    assert ('-u', 'request.txt', 'request.txt') in rsts
    assert ('-u', 'request.txt', 'urgency') in rsts
    assert ('-u', 'urgency', 'request.txt') in rsts
    assert ('-u', 'urgency', 'urgency') in rsts

    print "tested", count, "possibilities",
    os.remove("temp.py")
    os.remove("temp.pyc")
