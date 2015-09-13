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
              '    ./kitchen burger [--raw | --medium | --overcooked]\\n'
              '    ./kitchen [-u <urgency>] <request>\\n'
              '    ./kitchen -h | --help | --version\\n'),
    'spec': [
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
}
"""
    with open("spec.py", "w") as f:
        f.write(spec)
    os.system("python lutline/main.py -l c -o cli.c spec.py")
    os.system("gcc -Wall -o cli cli.c")

    count = 0
    rsts = []
    samples = ['burger', '--raw', '-raws', '--medium', '-meds',
               '--overcooked', '-overc']
    for i in range(2 + 1):
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

    assert len(rsts) == 4
    assert ('burger',) in rsts
    assert ('burger', '--raw') in rsts
    assert ('burger', '--medium') in rsts
    assert ('burger', '--overcooked') in rsts

    rsts = []
    samples = ['-u', '--u', '-u1', 'request.txt', 'urgency',
               '--version', '-v', '--help', '-h', '--h', '-help']
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
    for fname in ["cli", "cli.c", "spec.py"]:
        try:
            os.remove(fname)
        except:
            pass
