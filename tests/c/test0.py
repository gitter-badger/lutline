#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import subprocess
import itertools



def run():
    spec = """\
{
    'usage': "usage: ./cli [-f <fout>] <fin>",
    'spec': [
        ['opt', [['f', 'f'], ['a', 'fout']]],
        ['a', 'fin']
    ]
}
"""
    with open("spec.py", "w") as f:
        f.write(spec)
    os.system("python lutline/main.py -l c -o cli.c spec.py")
    os.system("gcc -Wall -o cli cli.c")

    count = 0
    rsts = []
    samples = ['file.txt', '-file.txt', '-f', '-f1', '-ff', '--f',
               '-a']
    for i in range(4):
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
    assert ('file.txt',) in rsts
    assert ('-f', 'file.txt', 'file.txt') in rsts

    print "tested", count, "possibilities",
    for fname in ["cli", "cli.c", "spec.py"]:
        try:
            os.remove(fname)
        except:
            pass


if __name__ == "__main__":
    run()
