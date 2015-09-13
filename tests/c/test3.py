#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools
import subprocess


def run():
    spec = r"""\
{
    'usage': ('Usage:\\n'
             '    ./hotel {-q (-v | -v1 | -v2)} <rooms>\\n'
             '    ./hotel -v [<request>]\\n'),
    'spec': [
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
}
"""
    with open("spec.py", "w") as f:
        f.write(spec)
    os.system("python lutline/main.py -l c -o cli.c spec.py")
    os.system("gcc -Wall -o cli cli.c")

    count = 0
    rsts = []
    samples = ['-v', '--v', '-v1', 'rooms.txt']
    for i in range(3 + 1):
        iterator = itertools.product(samples, repeat=i)
        for op in iterator:
            count += 1
            cmd = ["./cli"] + list(op)
            try:
                rst = subprocess.check_output(cmd, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError:
                pass
            else:
                rsts.append(op)

    assert len(rsts) == 2
    assert ('-v',) in rsts
    assert ('-v', 'rooms.txt') in rsts

    rsts = []
    samples = ['-q', '-v', '-v1', '-v2', '--v', 'rooms.txt']
    for i in range(3 + 1):
        iterator = itertools.product(samples, repeat=i)
        for op in iterator:
            count += 1
            cmd = ["./cli"] + list(op)
            try:
                rst = subprocess.check_output(cmd, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError:
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
    for fname in ["cli", "cli.c", "spec.py"]:
        try:
            os.remove(fname)
        except:
            pass
