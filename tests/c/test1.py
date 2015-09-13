#!/usr/bin/env python
#-*- coding:utf-8 -*-


import importlib
import os
import itertools
import subprocess


def run():
    spec = """\
{
    'usage': "usage: (...)",
    'spec': [
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
}
"""
    with open("spec.py", "w") as f:
        f.write(spec)
    os.system("python lutline/main.py -l c -o cli.c spec.py")
    os.system("gcc -Wall -o cli cli.c")

    count = 0
    rsts = []
    samples = ['-l', '--l', '-o', '-o1', 'file.txt']
    for i in range(5 + 1):
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
    assert ('file.txt',) in rsts
    assert ('-l', 'file.txt', 'file.txt') in rsts
    assert ('-o', 'file.txt', 'file.txt') in rsts
    assert ('-l', 'file.txt', '-o', 'file.txt', 'file.txt') in rsts

    rsts = []
    samples = ['dump', 'file_txt', '-f']
    for i in range(5 + 1):
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
    assert ('dump',) in rsts
    assert ('file_txt',) in rsts
    assert ('dump', 'dump') in rsts
    assert ('dump', 'file_txt') in rsts

    print "tested", count, "possibilities",
    for fname in ["cli", "cli.c", "spec.py"]:
        try:
            os.remove(fname)
        except:
            pass
