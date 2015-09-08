#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import subprocess
import multiprocessing


def run():
    spec = """\
usage = "usage: ./app [-f <fout>] <fin>"
spec = [
    ['opt', [['f', 'f'], ['a', 'fout']]],
    ['a', 'fin']
]
"""
    with open("spec.py", "w") as f:
        f.write(spec)
    os.system("python lutline/main.py -l c -o cli.c spec.py")
    os.system("gcc -Wall -o cli cli.c")
    return

    # We are about to try 780 argv combinations. No problem
    args = [
        [],
        ["-f"],
        ["-t"],
        ["--f"],
        ["-f1"],
        ["ola.txt"],
        ["-f", "-f"],
        ["-f", "-t"],
        ["-f", "--f"],
        ["-f", "-f1"],
        ["-f", "ola.txt"],
        ["-t", "-f"],
        ["-t", "-t"],
        ["-t", "--f"],
        ["-t", "-f1"],
        ["-t", "ola.txt"],
        ["--f", "-f"],
        ["--f", "-t"],
        ["--f", "--f"],
        ["--f", "-f1"],
        ["--f", "ola.txt"],
        ["-f1", "-f"],
        ["-f1", "-t"],
        ["-f1", "--f"],
        ["-f1", "-f1"],
        ["-f1", "ola.txt"],
        ["ola.txt", "-f"],
        ["ola.txt", "-t"],
        ["ola.txt", "--f"],
        ["ola.txt", "-f1"],
        ["ola.txt", "ola.txt"],
        ["-f", "-f", "-f"],
        ["-f", "-f", "-t"],
        ["-f", "-f", "--f"],
        ["-f", "-f", "-f1"],
        ["-f", "-f", "ola.txt"],
        ["-f", "-t", "-f"],
        ["-f", "-t", "-t"],
        ["-f", "-t", "--f"],
        ["-f", "-t", "-f1"],
        ["-f", "-t", "ola.txt"],
        ["-f", "--f", "-f"],
        ["-f", "--f", "-t"],
        ["-f", "--f", "--f"],
        ["-f", "--f", "-f1"],
        ["-f", "--f", "ola.txt"],
        ["-f", "-f1", "-f"],
        ["-f", "-f1", "-t"],
        ["-f", "-f1", "--f"],
        ["-f", "-f1", "-f1"],
        ["-f", "-f1", "ola.txt"],
        ["-f", "ola.txt", "-f"],
        ["-f", "ola.txt", "-t"],
        ["-f", "ola.txt", "--f"],
        ["-f", "ola.txt", "-f1"],
        ["-f", "ola.txt", "ola.txt"],
        ["-t", "-f", "-f"],
        ["-t", "-f", "-t"],
        ["-t", "-f", "--f"],
        ["-t", "-f", "-f1"],
        ["-t", "-f", "ola.txt"],
        ["-t", "-t", "-f"],
        ["-t", "-t", "-t"],
        ["-t", "-t", "--f"],
        ["-t", "-t", "-f1"],
        ["-t", "-t", "ola.txt"],
        ["-t", "--f", "-f"],
        ["-t", "--f", "-t"],
        ["-t", "--f", "--f"],
        ["-t", "--f", "-f1"],
        ["-t", "--f", "ola.txt"],
        ["-t", "-f1", "-f"],
        ["-t", "-f1", "-t"],
        ["-t", "-f1", "--f"],
        ["-t", "-f1", "-f1"],
        ["-t", "-f1", "ola.txt"],
        ["-t", "ola.txt", "-f"],
        ["-t", "ola.txt", "-t"],
        ["-t", "ola.txt", "--f"],
        ["-t", "ola.txt", "-f1"],
        ["-t", "ola.txt", "ola.txt"],
        ["--f", "-f", "-f"],
        ["--f", "-f", "-t"],
        ["--f", "-f", "--f"],
        ["--f", "-f", "-f1"],
        ["--f", "-f", "ola.txt"],
        ["--f", "-t", "-f"],
        ["--f", "-t", "-t"],
        ["--f", "-t", "--f"],
        ["--f", "-t", "-f1"],
        ["--f", "-t", "ola.txt"],
        ["--f", "--f", "-f"],
        ["--f", "--f", "-t"],
        ["--f", "--f", "--f"],
        ["--f", "--f", "-f1"],
        ["--f", "--f", "ola.txt"],
        ["--f", "-f1", "-f"],
        ["--f", "-f1", "-t"],
        ["--f", "-f1", "--f"],
        ["--f", "-f1", "-f1"],
        ["--f", "-f1", "ola.txt"],
        ["--f", "ola.txt", "-f"],
        ["--f", "ola.txt", "-t"],
        ["--f", "ola.txt", "--f"],
        ["--f", "ola.txt", "-f1"],
        ["--f", "ola.txt", "ola.txt"],
        ["-f1", "-f", "-f"],
        ["-f1", "-f", "-t"],
        ["-f1", "-f", "--f"],
        ["-f1", "-f", "-f1"],
        ["-f1", "-f", "ola.txt"],
        ["-f1", "-t", "-f"],
        ["-f1", "-t", "-t"],
        ["-f1", "-t", "--f"],
        ["-f1", "-t", "-f1"],
        ["-f1", "-t", "ola.txt"],
        ["-f1", "--f", "-f"],
        ["-f1", "--f", "-t"],
        ["-f1", "--f", "--f"],
        ["-f1", "--f", "-f1"],
        ["-f1", "--f", "ola.txt"],
        ["-f1", "-f1", "-f"],
        ["-f1", "-f1", "-t"],
        ["-f1", "-f1", "--f"],
        ["-f1", "-f1", "-f1"],
        ["-f1", "-f1", "ola.txt"],
        ["-f1", "ola.txt", "-f"],
        ["-f1", "ola.txt", "-t"],
        ["-f1", "ola.txt", "--f"],
        ["-f1", "ola.txt", "-f1"],
        ["-f1", "ola.txt", "ola.txt"],
        ["ola.txt", "-f", "-f"],
        ["ola.txt", "-f", "-t"],
        ["ola.txt", "-f", "--f"],
        ["ola.txt", "-f", "-f1"],
        ["ola.txt", "-f", "ola.txt"],
        ["ola.txt", "-t", "-f"],
        ["ola.txt", "-t", "-t"],
        ["ola.txt", "-t", "--f"],
        ["ola.txt", "-t", "-f1"],
        ["ola.txt", "-t", "ola.txt"],
        ["ola.txt", "--f", "-f"],
        ["ola.txt", "--f", "-t"],
        ["ola.txt", "--f", "--f"],
        ["ola.txt", "--f", "-f1"],
        ["ola.txt", "--f", "ola.txt"],
        ["ola.txt", "-f1", "-f"],
        ["ola.txt", "-f1", "-t"],
        ["ola.txt", "-f1", "--f"],
        ["ola.txt", "-f1", "-f1"],
        ["ola.txt", "-f1", "ola.txt"],
        ["ola.txt", "ola.txt", "-f"],
        ["ola.txt", "ola.txt", "-t"],
        ["ola.txt", "ola.txt", "--f"],
        ["ola.txt", "ola.txt", "-f1"],
        ["ola.txt", "ola.txt", "ola.txt"],
        ["-f", "-f", "-f", "-f"],
        ["-f", "-f", "-f", "-t"],
        ["-f", "-f", "-f", "--f"],
        ["-f", "-f", "-f", "-f1"],
        ["-f", "-f", "-f", "ola.txt"],
        ["-f", "-f", "-t", "-f"],
        ["-f", "-f", "-t", "-t"],
        ["-f", "-f", "-t", "--f"],
        ["-f", "-f", "-t", "-f1"],
        ["-f", "-f", "-t", "ola.txt"],
        ["-f", "-f", "--f", "-f"],
        ["-f", "-f", "--f", "-t"],
        ["-f", "-f", "--f", "--f"],
        ["-f", "-f", "--f", "-f1"],
        ["-f", "-f", "--f", "ola.txt"],
        ["-f", "-f", "-f1", "-f"],
        ["-f", "-f", "-f1", "-t"],
        ["-f", "-f", "-f1", "--f"],
        ["-f", "-f", "-f1", "-f1"],
        ["-f", "-f", "-f1", "ola.txt"],
        ["-f", "-f", "ola.txt", "-f"],
        ["-f", "-f", "ola.txt", "-t"],
        ["-f", "-f", "ola.txt", "--f"],
        ["-f", "-f", "ola.txt", "-f1"],
        ["-f", "-f", "ola.txt", "ola.txt"],
        ["-f", "-t", "-f", "-f"],
        ["-f", "-t", "-f", "-t"],
        ["-f", "-t", "-f", "--f"],
        ["-f", "-t", "-f", "-f1"],
        ["-f", "-t", "-f", "ola.txt"],
        ["-f", "-t", "-t", "-f"],
        ["-f", "-t", "-t", "-t"],
        ["-f", "-t", "-t", "--f"],
        ["-f", "-t", "-t", "-f1"],
        ["-f", "-t", "-t", "ola.txt"],
        ["-f", "-t", "--f", "-f"],
        ["-f", "-t", "--f", "-t"],
        ["-f", "-t", "--f", "--f"],
        ["-f", "-t", "--f", "-f1"],
        ["-f", "-t", "--f", "ola.txt"],
        ["-f", "-t", "-f1", "-f"],
        ["-f", "-t", "-f1", "-t"],
        ["-f", "-t", "-f1", "--f"],
        ["-f", "-t", "-f1", "-f1"],
        ["-f", "-t", "-f1", "ola.txt"],
        ["-f", "-t", "ola.txt", "-f"],
        ["-f", "-t", "ola.txt", "-t"],
        ["-f", "-t", "ola.txt", "--f"],
        ["-f", "-t", "ola.txt", "-f1"],
        ["-f", "-t", "ola.txt", "ola.txt"],
        ["-f", "--f", "-f", "-f"],
        ["-f", "--f", "-f", "-t"],
        ["-f", "--f", "-f", "--f"],
        ["-f", "--f", "-f", "-f1"],
        ["-f", "--f", "-f", "ola.txt"],
        ["-f", "--f", "-t", "-f"],
        ["-f", "--f", "-t", "-t"],
        ["-f", "--f", "-t", "--f"],
        ["-f", "--f", "-t", "-f1"],
        ["-f", "--f", "-t", "ola.txt"],
        ["-f", "--f", "--f", "-f"],
        ["-f", "--f", "--f", "-t"],
        ["-f", "--f", "--f", "--f"],
        ["-f", "--f", "--f", "-f1"],
        ["-f", "--f", "--f", "ola.txt"],
        ["-f", "--f", "-f1", "-f"],
        ["-f", "--f", "-f1", "-t"],
        ["-f", "--f", "-f1", "--f"],
        ["-f", "--f", "-f1", "-f1"],
        ["-f", "--f", "-f1", "ola.txt"],
        ["-f", "--f", "ola.txt", "-f"],
        ["-f", "--f", "ola.txt", "-t"],
        ["-f", "--f", "ola.txt", "--f"],
        ["-f", "--f", "ola.txt", "-f1"],
        ["-f", "--f", "ola.txt", "ola.txt"],
        ["-f", "-f1", "-f", "-f"],
        ["-f", "-f1", "-f", "-t"],
        ["-f", "-f1", "-f", "--f"],
        ["-f", "-f1", "-f", "-f1"],
        ["-f", "-f1", "-f", "ola.txt"],
        ["-f", "-f1", "-t", "-f"],
        ["-f", "-f1", "-t", "-t"],
        ["-f", "-f1", "-t", "--f"],
        ["-f", "-f1", "-t", "-f1"],
        ["-f", "-f1", "-t", "ola.txt"],
        ["-f", "-f1", "--f", "-f"],
        ["-f", "-f1", "--f", "-t"],
        ["-f", "-f1", "--f", "--f"],
        ["-f", "-f1", "--f", "-f1"],
        ["-f", "-f1", "--f", "ola.txt"],
        ["-f", "-f1", "-f1", "-f"],
        ["-f", "-f1", "-f1", "-t"],
        ["-f", "-f1", "-f1", "--f"],
        ["-f", "-f1", "-f1", "-f1"],
        ["-f", "-f1", "-f1", "ola.txt"],
        ["-f", "-f1", "ola.txt", "-f"],
        ["-f", "-f1", "ola.txt", "-t"],
        ["-f", "-f1", "ola.txt", "--f"],
        ["-f", "-f1", "ola.txt", "-f1"],
        ["-f", "-f1", "ola.txt", "ola.txt"],
        ["-f", "ola.txt", "-f", "-f"],
        ["-f", "ola.txt", "-f", "-t"],
        ["-f", "ola.txt", "-f", "--f"],
        ["-f", "ola.txt", "-f", "-f1"],
        ["-f", "ola.txt", "-f", "ola.txt"],
        ["-f", "ola.txt", "-t", "-f"],
        ["-f", "ola.txt", "-t", "-t"],
        ["-f", "ola.txt", "-t", "--f"],
        ["-f", "ola.txt", "-t", "-f1"],
        ["-f", "ola.txt", "-t", "ola.txt"],
        ["-f", "ola.txt", "--f", "-f"],
        ["-f", "ola.txt", "--f", "-t"],
        ["-f", "ola.txt", "--f", "--f"],
        ["-f", "ola.txt", "--f", "-f1"],
        ["-f", "ola.txt", "--f", "ola.txt"],
        ["-f", "ola.txt", "-f1", "-f"],
        ["-f", "ola.txt", "-f1", "-t"],
        ["-f", "ola.txt", "-f1", "--f"],
        ["-f", "ola.txt", "-f1", "-f1"],
        ["-f", "ola.txt", "-f1", "ola.txt"],
        ["-f", "ola.txt", "ola.txt", "-f"],
        ["-f", "ola.txt", "ola.txt", "-t"],
        ["-f", "ola.txt", "ola.txt", "--f"],
        ["-f", "ola.txt", "ola.txt", "-f1"],
        ["-f", "ola.txt", "ola.txt", "ola.txt"],
        ["-t", "-f", "-f", "-f"],
        ["-t", "-f", "-f", "-t"],
        ["-t", "-f", "-f", "--f"],
        ["-t", "-f", "-f", "-f1"],
        ["-t", "-f", "-f", "ola.txt"],
        ["-t", "-f", "-t", "-f"],
        ["-t", "-f", "-t", "-t"],
        ["-t", "-f", "-t", "--f"],
        ["-t", "-f", "-t", "-f1"],
        ["-t", "-f", "-t", "ola.txt"],
        ["-t", "-f", "--f", "-f"],
        ["-t", "-f", "--f", "-t"],
        ["-t", "-f", "--f", "--f"],
        ["-t", "-f", "--f", "-f1"],
        ["-t", "-f", "--f", "ola.txt"],
        ["-t", "-f", "-f1", "-f"],
        ["-t", "-f", "-f1", "-t"],
        ["-t", "-f", "-f1", "--f"],
        ["-t", "-f", "-f1", "-f1"],
        ["-t", "-f", "-f1", "ola.txt"],
        ["-t", "-f", "ola.txt", "-f"],
        ["-t", "-f", "ola.txt", "-t"],
        ["-t", "-f", "ola.txt", "--f"],
        ["-t", "-f", "ola.txt", "-f1"],
        ["-t", "-f", "ola.txt", "ola.txt"],
        ["-t", "-t", "-f", "-f"],
        ["-t", "-t", "-f", "-t"],
        ["-t", "-t", "-f", "--f"],
        ["-t", "-t", "-f", "-f1"],
        ["-t", "-t", "-f", "ola.txt"],
        ["-t", "-t", "-t", "-f"],
        ["-t", "-t", "-t", "-t"],
        ["-t", "-t", "-t", "--f"],
        ["-t", "-t", "-t", "-f1"],
        ["-t", "-t", "-t", "ola.txt"],
        ["-t", "-t", "--f", "-f"],
        ["-t", "-t", "--f", "-t"],
        ["-t", "-t", "--f", "--f"],
        ["-t", "-t", "--f", "-f1"],
        ["-t", "-t", "--f", "ola.txt"],
        ["-t", "-t", "-f1", "-f"],
        ["-t", "-t", "-f1", "-t"],
        ["-t", "-t", "-f1", "--f"],
        ["-t", "-t", "-f1", "-f1"],
        ["-t", "-t", "-f1", "ola.txt"],
        ["-t", "-t", "ola.txt", "-f"],
        ["-t", "-t", "ola.txt", "-t"],
        ["-t", "-t", "ola.txt", "--f"],
        ["-t", "-t", "ola.txt", "-f1"],
        ["-t", "-t", "ola.txt", "ola.txt"],
        ["-t", "--f", "-f", "-f"],
        ["-t", "--f", "-f", "-t"],
        ["-t", "--f", "-f", "--f"],
        ["-t", "--f", "-f", "-f1"],
        ["-t", "--f", "-f", "ola.txt"],
        ["-t", "--f", "-t", "-f"],
        ["-t", "--f", "-t", "-t"],
        ["-t", "--f", "-t", "--f"],
        ["-t", "--f", "-t", "-f1"],
        ["-t", "--f", "-t", "ola.txt"],
        ["-t", "--f", "--f", "-f"],
        ["-t", "--f", "--f", "-t"],
        ["-t", "--f", "--f", "--f"],
        ["-t", "--f", "--f", "-f1"],
        ["-t", "--f", "--f", "ola.txt"],
        ["-t", "--f", "-f1", "-f"],
        ["-t", "--f", "-f1", "-t"],
        ["-t", "--f", "-f1", "--f"],
        ["-t", "--f", "-f1", "-f1"],
        ["-t", "--f", "-f1", "ola.txt"],
        ["-t", "--f", "ola.txt", "-f"],
        ["-t", "--f", "ola.txt", "-t"],
        ["-t", "--f", "ola.txt", "--f"],
        ["-t", "--f", "ola.txt", "-f1"],
        ["-t", "--f", "ola.txt", "ola.txt"],
        ["-t", "-f1", "-f", "-f"],
        ["-t", "-f1", "-f", "-t"],
        ["-t", "-f1", "-f", "--f"],
        ["-t", "-f1", "-f", "-f1"],
        ["-t", "-f1", "-f", "ola.txt"],
        ["-t", "-f1", "-t", "-f"],
        ["-t", "-f1", "-t", "-t"],
        ["-t", "-f1", "-t", "--f"],
        ["-t", "-f1", "-t", "-f1"],
        ["-t", "-f1", "-t", "ola.txt"],
        ["-t", "-f1", "--f", "-f"],
        ["-t", "-f1", "--f", "-t"],
        ["-t", "-f1", "--f", "--f"],
        ["-t", "-f1", "--f", "-f1"],
        ["-t", "-f1", "--f", "ola.txt"],
        ["-t", "-f1", "-f1", "-f"],
        ["-t", "-f1", "-f1", "-t"],
        ["-t", "-f1", "-f1", "--f"],
        ["-t", "-f1", "-f1", "-f1"],
        ["-t", "-f1", "-f1", "ola.txt"],
        ["-t", "-f1", "ola.txt", "-f"],
        ["-t", "-f1", "ola.txt", "-t"],
        ["-t", "-f1", "ola.txt", "--f"],
        ["-t", "-f1", "ola.txt", "-f1"],
        ["-t", "-f1", "ola.txt", "ola.txt"],
        ["-t", "ola.txt", "-f", "-f"],
        ["-t", "ola.txt", "-f", "-t"],
        ["-t", "ola.txt", "-f", "--f"],
        ["-t", "ola.txt", "-f", "-f1"],
        ["-t", "ola.txt", "-f", "ola.txt"],
        ["-t", "ola.txt", "-t", "-f"],
        ["-t", "ola.txt", "-t", "-t"],
        ["-t", "ola.txt", "-t", "--f"],
        ["-t", "ola.txt", "-t", "-f1"],
        ["-t", "ola.txt", "-t", "ola.txt"],
        ["-t", "ola.txt", "--f", "-f"],
        ["-t", "ola.txt", "--f", "-t"],
        ["-t", "ola.txt", "--f", "--f"],
        ["-t", "ola.txt", "--f", "-f1"],
        ["-t", "ola.txt", "--f", "ola.txt"],
        ["-t", "ola.txt", "-f1", "-f"],
        ["-t", "ola.txt", "-f1", "-t"],
        ["-t", "ola.txt", "-f1", "--f"],
        ["-t", "ola.txt", "-f1", "-f1"],
        ["-t", "ola.txt", "-f1", "ola.txt"],
        ["-t", "ola.txt", "ola.txt", "-f"],
        ["-t", "ola.txt", "ola.txt", "-t"],
        ["-t", "ola.txt", "ola.txt", "--f"],
        ["-t", "ola.txt", "ola.txt", "-f1"],
        ["-t", "ola.txt", "ola.txt", "ola.txt"],
        ["--f", "-f", "-f", "-f"],
        ["--f", "-f", "-f", "-t"],
        ["--f", "-f", "-f", "--f"],
        ["--f", "-f", "-f", "-f1"],
        ["--f", "-f", "-f", "ola.txt"],
        ["--f", "-f", "-t", "-f"],
        ["--f", "-f", "-t", "-t"],
        ["--f", "-f", "-t", "--f"],
        ["--f", "-f", "-t", "-f1"],
        ["--f", "-f", "-t", "ola.txt"],
        ["--f", "-f", "--f", "-f"],
        ["--f", "-f", "--f", "-t"],
        ["--f", "-f", "--f", "--f"],
        ["--f", "-f", "--f", "-f1"],
        ["--f", "-f", "--f", "ola.txt"],
        ["--f", "-f", "-f1", "-f"],
        ["--f", "-f", "-f1", "-t"],
        ["--f", "-f", "-f1", "--f"],
        ["--f", "-f", "-f1", "-f1"],
        ["--f", "-f", "-f1", "ola.txt"],
        ["--f", "-f", "ola.txt", "-f"],
        ["--f", "-f", "ola.txt", "-t"],
        ["--f", "-f", "ola.txt", "--f"],
        ["--f", "-f", "ola.txt", "-f1"],
        ["--f", "-f", "ola.txt", "ola.txt"],
        ["--f", "-t", "-f", "-f"],
        ["--f", "-t", "-f", "-t"],
        ["--f", "-t", "-f", "--f"],
        ["--f", "-t", "-f", "-f1"],
        ["--f", "-t", "-f", "ola.txt"],
        ["--f", "-t", "-t", "-f"],
        ["--f", "-t", "-t", "-t"],
        ["--f", "-t", "-t", "--f"],
        ["--f", "-t", "-t", "-f1"],
        ["--f", "-t", "-t", "ola.txt"],
        ["--f", "-t", "--f", "-f"],
        ["--f", "-t", "--f", "-t"],
        ["--f", "-t", "--f", "--f"],
        ["--f", "-t", "--f", "-f1"],
        ["--f", "-t", "--f", "ola.txt"],
        ["--f", "-t", "-f1", "-f"],
        ["--f", "-t", "-f1", "-t"],
        ["--f", "-t", "-f1", "--f"],
        ["--f", "-t", "-f1", "-f1"],
        ["--f", "-t", "-f1", "ola.txt"],
        ["--f", "-t", "ola.txt", "-f"],
        ["--f", "-t", "ola.txt", "-t"],
        ["--f", "-t", "ola.txt", "--f"],
        ["--f", "-t", "ola.txt", "-f1"],
        ["--f", "-t", "ola.txt", "ola.txt"],
        ["--f", "--f", "-f", "-f"],
        ["--f", "--f", "-f", "-t"],
        ["--f", "--f", "-f", "--f"],
        ["--f", "--f", "-f", "-f1"],
        ["--f", "--f", "-f", "ola.txt"],
        ["--f", "--f", "-t", "-f"],
        ["--f", "--f", "-t", "-t"],
        ["--f", "--f", "-t", "--f"],
        ["--f", "--f", "-t", "-f1"],
        ["--f", "--f", "-t", "ola.txt"],
        ["--f", "--f", "--f", "-f"],
        ["--f", "--f", "--f", "-t"],
        ["--f", "--f", "--f", "--f"],
        ["--f", "--f", "--f", "-f1"],
        ["--f", "--f", "--f", "ola.txt"],
        ["--f", "--f", "-f1", "-f"],
        ["--f", "--f", "-f1", "-t"],
        ["--f", "--f", "-f1", "--f"],
        ["--f", "--f", "-f1", "-f1"],
        ["--f", "--f", "-f1", "ola.txt"],
        ["--f", "--f", "ola.txt", "-f"],
        ["--f", "--f", "ola.txt", "-t"],
        ["--f", "--f", "ola.txt", "--f"],
        ["--f", "--f", "ola.txt", "-f1"],
        ["--f", "--f", "ola.txt", "ola.txt"],
        ["--f", "-f1", "-f", "-f"],
        ["--f", "-f1", "-f", "-t"],
        ["--f", "-f1", "-f", "--f"],
        ["--f", "-f1", "-f", "-f1"],
        ["--f", "-f1", "-f", "ola.txt"],
        ["--f", "-f1", "-t", "-f"],
        ["--f", "-f1", "-t", "-t"],
        ["--f", "-f1", "-t", "--f"],
        ["--f", "-f1", "-t", "-f1"],
        ["--f", "-f1", "-t", "ola.txt"],
        ["--f", "-f1", "--f", "-f"],
        ["--f", "-f1", "--f", "-t"],
        ["--f", "-f1", "--f", "--f"],
        ["--f", "-f1", "--f", "-f1"],
        ["--f", "-f1", "--f", "ola.txt"],
        ["--f", "-f1", "-f1", "-f"],
        ["--f", "-f1", "-f1", "-t"],
        ["--f", "-f1", "-f1", "--f"],
        ["--f", "-f1", "-f1", "-f1"],
        ["--f", "-f1", "-f1", "ola.txt"],
        ["--f", "-f1", "ola.txt", "-f"],
        ["--f", "-f1", "ola.txt", "-t"],
        ["--f", "-f1", "ola.txt", "--f"],
        ["--f", "-f1", "ola.txt", "-f1"],
        ["--f", "-f1", "ola.txt", "ola.txt"],
        ["--f", "ola.txt", "-f", "-f"],
        ["--f", "ola.txt", "-f", "-t"],
        ["--f", "ola.txt", "-f", "--f"],
        ["--f", "ola.txt", "-f", "-f1"],
        ["--f", "ola.txt", "-f", "ola.txt"],
        ["--f", "ola.txt", "-t", "-f"],
        ["--f", "ola.txt", "-t", "-t"],
        ["--f", "ola.txt", "-t", "--f"],
        ["--f", "ola.txt", "-t", "-f1"],
        ["--f", "ola.txt", "-t", "ola.txt"],
        ["--f", "ola.txt", "--f", "-f"],
        ["--f", "ola.txt", "--f", "-t"],
        ["--f", "ola.txt", "--f", "--f"],
        ["--f", "ola.txt", "--f", "-f1"],
        ["--f", "ola.txt", "--f", "ola.txt"],
        ["--f", "ola.txt", "-f1", "-f"],
        ["--f", "ola.txt", "-f1", "-t"],
        ["--f", "ola.txt", "-f1", "--f"],
        ["--f", "ola.txt", "-f1", "-f1"],
        ["--f", "ola.txt", "-f1", "ola.txt"],
        ["--f", "ola.txt", "ola.txt", "-f"],
        ["--f", "ola.txt", "ola.txt", "-t"],
        ["--f", "ola.txt", "ola.txt", "--f"],
        ["--f", "ola.txt", "ola.txt", "-f1"],
        ["--f", "ola.txt", "ola.txt", "ola.txt"],
        ["-f1", "-f", "-f", "-f"],
        ["-f1", "-f", "-f", "-t"],
        ["-f1", "-f", "-f", "--f"],
        ["-f1", "-f", "-f", "-f1"],
        ["-f1", "-f", "-f", "ola.txt"],
        ["-f1", "-f", "-t", "-f"],
        ["-f1", "-f", "-t", "-t"],
        ["-f1", "-f", "-t", "--f"],
        ["-f1", "-f", "-t", "-f1"],
        ["-f1", "-f", "-t", "ola.txt"],
        ["-f1", "-f", "--f", "-f"],
        ["-f1", "-f", "--f", "-t"],
        ["-f1", "-f", "--f", "--f"],
        ["-f1", "-f", "--f", "-f1"],
        ["-f1", "-f", "--f", "ola.txt"],
        ["-f1", "-f", "-f1", "-f"],
        ["-f1", "-f", "-f1", "-t"],
        ["-f1", "-f", "-f1", "--f"],
        ["-f1", "-f", "-f1", "-f1"],
        ["-f1", "-f", "-f1", "ola.txt"],
        ["-f1", "-f", "ola.txt", "-f"],
        ["-f1", "-f", "ola.txt", "-t"],
        ["-f1", "-f", "ola.txt", "--f"],
        ["-f1", "-f", "ola.txt", "-f1"],
        ["-f1", "-f", "ola.txt", "ola.txt"],
        ["-f1", "-t", "-f", "-f"],
        ["-f1", "-t", "-f", "-t"],
        ["-f1", "-t", "-f", "--f"],
        ["-f1", "-t", "-f", "-f1"],
        ["-f1", "-t", "-f", "ola.txt"],
        ["-f1", "-t", "-t", "-f"],
        ["-f1", "-t", "-t", "-t"],
        ["-f1", "-t", "-t", "--f"],
        ["-f1", "-t", "-t", "-f1"],
        ["-f1", "-t", "-t", "ola.txt"],
        ["-f1", "-t", "--f", "-f"],
        ["-f1", "-t", "--f", "-t"],
        ["-f1", "-t", "--f", "--f"],
        ["-f1", "-t", "--f", "-f1"],
        ["-f1", "-t", "--f", "ola.txt"],
        ["-f1", "-t", "-f1", "-f"],
        ["-f1", "-t", "-f1", "-t"],
        ["-f1", "-t", "-f1", "--f"],
        ["-f1", "-t", "-f1", "-f1"],
        ["-f1", "-t", "-f1", "ola.txt"],
        ["-f1", "-t", "ola.txt", "-f"],
        ["-f1", "-t", "ola.txt", "-t"],
        ["-f1", "-t", "ola.txt", "--f"],
        ["-f1", "-t", "ola.txt", "-f1"],
        ["-f1", "-t", "ola.txt", "ola.txt"],
        ["-f1", "--f", "-f", "-f"],
        ["-f1", "--f", "-f", "-t"],
        ["-f1", "--f", "-f", "--f"],
        ["-f1", "--f", "-f", "-f1"],
        ["-f1", "--f", "-f", "ola.txt"],
        ["-f1", "--f", "-t", "-f"],
        ["-f1", "--f", "-t", "-t"],
        ["-f1", "--f", "-t", "--f"],
        ["-f1", "--f", "-t", "-f1"],
        ["-f1", "--f", "-t", "ola.txt"],
        ["-f1", "--f", "--f", "-f"],
        ["-f1", "--f", "--f", "-t"],
        ["-f1", "--f", "--f", "--f"],
        ["-f1", "--f", "--f", "-f1"],
        ["-f1", "--f", "--f", "ola.txt"],
        ["-f1", "--f", "-f1", "-f"],
        ["-f1", "--f", "-f1", "-t"],
        ["-f1", "--f", "-f1", "--f"],
        ["-f1", "--f", "-f1", "-f1"],
        ["-f1", "--f", "-f1", "ola.txt"],
        ["-f1", "--f", "ola.txt", "-f"],
        ["-f1", "--f", "ola.txt", "-t"],
        ["-f1", "--f", "ola.txt", "--f"],
        ["-f1", "--f", "ola.txt", "-f1"],
        ["-f1", "--f", "ola.txt", "ola.txt"],
        ["-f1", "-f1", "-f", "-f"],
        ["-f1", "-f1", "-f", "-t"],
        ["-f1", "-f1", "-f", "--f"],
        ["-f1", "-f1", "-f", "-f1"],
        ["-f1", "-f1", "-f", "ola.txt"],
        ["-f1", "-f1", "-t", "-f"],
        ["-f1", "-f1", "-t", "-t"],
        ["-f1", "-f1", "-t", "--f"],
        ["-f1", "-f1", "-t", "-f1"],
        ["-f1", "-f1", "-t", "ola.txt"],
        ["-f1", "-f1", "--f", "-f"],
        ["-f1", "-f1", "--f", "-t"],
        ["-f1", "-f1", "--f", "--f"],
        ["-f1", "-f1", "--f", "-f1"],
        ["-f1", "-f1", "--f", "ola.txt"],
        ["-f1", "-f1", "-f1", "-f"],
        ["-f1", "-f1", "-f1", "-t"],
        ["-f1", "-f1", "-f1", "--f"],
        ["-f1", "-f1", "-f1", "-f1"],
        ["-f1", "-f1", "-f1", "ola.txt"],
        ["-f1", "-f1", "ola.txt", "-f"],
        ["-f1", "-f1", "ola.txt", "-t"],
        ["-f1", "-f1", "ola.txt", "--f"],
        ["-f1", "-f1", "ola.txt", "-f1"],
        ["-f1", "-f1", "ola.txt", "ola.txt"],
        ["-f1", "ola.txt", "-f", "-f"],
        ["-f1", "ola.txt", "-f", "-t"],
        ["-f1", "ola.txt", "-f", "--f"],
        ["-f1", "ola.txt", "-f", "-f1"],
        ["-f1", "ola.txt", "-f", "ola.txt"],
        ["-f1", "ola.txt", "-t", "-f"],
        ["-f1", "ola.txt", "-t", "-t"],
        ["-f1", "ola.txt", "-t", "--f"],
        ["-f1", "ola.txt", "-t", "-f1"],
        ["-f1", "ola.txt", "-t", "ola.txt"],
        ["-f1", "ola.txt", "--f", "-f"],
        ["-f1", "ola.txt", "--f", "-t"],
        ["-f1", "ola.txt", "--f", "--f"],
        ["-f1", "ola.txt", "--f", "-f1"],
        ["-f1", "ola.txt", "--f", "ola.txt"],
        ["-f1", "ola.txt", "-f1", "-f"],
        ["-f1", "ola.txt", "-f1", "-t"],
        ["-f1", "ola.txt", "-f1", "--f"],
        ["-f1", "ola.txt", "-f1", "-f1"],
        ["-f1", "ola.txt", "-f1", "ola.txt"],
        ["-f1", "ola.txt", "ola.txt", "-f"],
        ["-f1", "ola.txt", "ola.txt", "-t"],
        ["-f1", "ola.txt", "ola.txt", "--f"],
        ["-f1", "ola.txt", "ola.txt", "-f1"],
        ["-f1", "ola.txt", "ola.txt", "ola.txt"],
        ["ola.txt", "-f", "-f", "-f"],
        ["ola.txt", "-f", "-f", "-t"],
        ["ola.txt", "-f", "-f", "--f"],
        ["ola.txt", "-f", "-f", "-f1"],
        ["ola.txt", "-f", "-f", "ola.txt"],
        ["ola.txt", "-f", "-t", "-f"],
        ["ola.txt", "-f", "-t", "-t"],
        ["ola.txt", "-f", "-t", "--f"],
        ["ola.txt", "-f", "-t", "-f1"],
        ["ola.txt", "-f", "-t", "ola.txt"],
        ["ola.txt", "-f", "--f", "-f"],
        ["ola.txt", "-f", "--f", "-t"],
        ["ola.txt", "-f", "--f", "--f"],
        ["ola.txt", "-f", "--f", "-f1"],
        ["ola.txt", "-f", "--f", "ola.txt"],
        ["ola.txt", "-f", "-f1", "-f"],
        ["ola.txt", "-f", "-f1", "-t"],
        ["ola.txt", "-f", "-f1", "--f"],
        ["ola.txt", "-f", "-f1", "-f1"],
        ["ola.txt", "-f", "-f1", "ola.txt"],
        ["ola.txt", "-f", "ola.txt", "-f"],
        ["ola.txt", "-f", "ola.txt", "-t"],
        ["ola.txt", "-f", "ola.txt", "--f"],
        ["ola.txt", "-f", "ola.txt", "-f1"],
        ["ola.txt", "-f", "ola.txt", "ola.txt"],
        ["ola.txt", "-t", "-f", "-f"],
        ["ola.txt", "-t", "-f", "-t"],
        ["ola.txt", "-t", "-f", "--f"],
        ["ola.txt", "-t", "-f", "-f1"],
        ["ola.txt", "-t", "-f", "ola.txt"],
        ["ola.txt", "-t", "-t", "-f"],
        ["ola.txt", "-t", "-t", "-t"],
        ["ola.txt", "-t", "-t", "--f"],
        ["ola.txt", "-t", "-t", "-f1"],
        ["ola.txt", "-t", "-t", "ola.txt"],
        ["ola.txt", "-t", "--f", "-f"],
        ["ola.txt", "-t", "--f", "-t"],
        ["ola.txt", "-t", "--f", "--f"],
        ["ola.txt", "-t", "--f", "-f1"],
        ["ola.txt", "-t", "--f", "ola.txt"],
        ["ola.txt", "-t", "-f1", "-f"],
        ["ola.txt", "-t", "-f1", "-t"],
        ["ola.txt", "-t", "-f1", "--f"],
        ["ola.txt", "-t", "-f1", "-f1"],
        ["ola.txt", "-t", "-f1", "ola.txt"],
        ["ola.txt", "-t", "ola.txt", "-f"],
        ["ola.txt", "-t", "ola.txt", "-t"],
        ["ola.txt", "-t", "ola.txt", "--f"],
        ["ola.txt", "-t", "ola.txt", "-f1"],
        ["ola.txt", "-t", "ola.txt", "ola.txt"],
        ["ola.txt", "--f", "-f", "-f"],
        ["ola.txt", "--f", "-f", "-t"],
        ["ola.txt", "--f", "-f", "--f"],
        ["ola.txt", "--f", "-f", "-f1"],
        ["ola.txt", "--f", "-f", "ola.txt"],
        ["ola.txt", "--f", "-t", "-f"],
        ["ola.txt", "--f", "-t", "-t"],
        ["ola.txt", "--f", "-t", "--f"],
        ["ola.txt", "--f", "-t", "-f1"],
        ["ola.txt", "--f", "-t", "ola.txt"],
        ["ola.txt", "--f", "--f", "-f"],
        ["ola.txt", "--f", "--f", "-t"],
        ["ola.txt", "--f", "--f", "--f"],
        ["ola.txt", "--f", "--f", "-f1"],
        ["ola.txt", "--f", "--f", "ola.txt"],
        ["ola.txt", "--f", "-f1", "-f"],
        ["ola.txt", "--f", "-f1", "-t"],
        ["ola.txt", "--f", "-f1", "--f"],
        ["ola.txt", "--f", "-f1", "-f1"],
        ["ola.txt", "--f", "-f1", "ola.txt"],
        ["ola.txt", "--f", "ola.txt", "-f"],
        ["ola.txt", "--f", "ola.txt", "-t"],
        ["ola.txt", "--f", "ola.txt", "--f"],
        ["ola.txt", "--f", "ola.txt", "-f1"],
        ["ola.txt", "--f", "ola.txt", "ola.txt"],
        ["ola.txt", "-f1", "-f", "-f"],
        ["ola.txt", "-f1", "-f", "-t"],
        ["ola.txt", "-f1", "-f", "--f"],
        ["ola.txt", "-f1", "-f", "-f1"],
        ["ola.txt", "-f1", "-f", "ola.txt"],
        ["ola.txt", "-f1", "-t", "-f"],
        ["ola.txt", "-f1", "-t", "-t"],
        ["ola.txt", "-f1", "-t", "--f"],
        ["ola.txt", "-f1", "-t", "-f1"],
        ["ola.txt", "-f1", "-t", "ola.txt"],
        ["ola.txt", "-f1", "--f", "-f"],
        ["ola.txt", "-f1", "--f", "-t"],
        ["ola.txt", "-f1", "--f", "--f"],
        ["ola.txt", "-f1", "--f", "-f1"],
        ["ola.txt", "-f1", "--f", "ola.txt"],
        ["ola.txt", "-f1", "-f1", "-f"],
        ["ola.txt", "-f1", "-f1", "-t"],
        ["ola.txt", "-f1", "-f1", "--f"],
        ["ola.txt", "-f1", "-f1", "-f1"],
        ["ola.txt", "-f1", "-f1", "ola.txt"],
        ["ola.txt", "-f1", "ola.txt", "-f"],
        ["ola.txt", "-f1", "ola.txt", "-t"],
        ["ola.txt", "-f1", "ola.txt", "--f"],
        ["ola.txt", "-f1", "ola.txt", "-f1"],
        ["ola.txt", "-f1", "ola.txt", "ola.txt"],
        ["ola.txt", "ola.txt", "-f", "-f"],
        ["ola.txt", "ola.txt", "-f", "-t"],
        ["ola.txt", "ola.txt", "-f", "--f"],
        ["ola.txt", "ola.txt", "-f", "-f1"],
        ["ola.txt", "ola.txt", "-f", "ola.txt"],
        ["ola.txt", "ola.txt", "-t", "-f"],
        ["ola.txt", "ola.txt", "-t", "-t"],
        ["ola.txt", "ola.txt", "-t", "--f"],
        ["ola.txt", "ola.txt", "-t", "-f1"],
        ["ola.txt", "ola.txt", "-t", "ola.txt"],
        ["ola.txt", "ola.txt", "--f", "-f"],
        ["ola.txt", "ola.txt", "--f", "-t"],
        ["ola.txt", "ola.txt", "--f", "--f"],
        ["ola.txt", "ola.txt", "--f", "-f1"],
        ["ola.txt", "ola.txt", "--f", "ola.txt"],
        ["ola.txt", "ola.txt", "-f1", "-f"],
        ["ola.txt", "ola.txt", "-f1", "-t"],
        ["ola.txt", "ola.txt", "-f1", "--f"],
        ["ola.txt", "ola.txt", "-f1", "-f1"],
        ["ola.txt", "ola.txt", "-f1", "ola.txt"],
        ["ola.txt", "ola.txt", "ola.txt", "-f"],
        ["ola.txt", "ola.txt", "ola.txt", "-t"],
        ["ola.txt", "ola.txt", "ola.txt", "--f"],
        ["ola.txt", "ola.txt", "ola.txt", "-f1"],
        ["ola.txt", "ola.txt", "ola.txt", "ola.txt"],
    ]

    count = 0
    rsts = []
    for arg in args:
        count += 1
        cmd = "python cli.py " + " ".join(arg)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        try:
            assert type(eval(out)) == dict
        except:
            pass
        else:
            rsts.append(arg)

    assert len(rsts) == 2
    assert ['ola.txt'] in rsts
    assert ['-f', 'ola.txt', 'ola.txt'] in rsts
    print "tested", count, "possibilities",

    os.remove("cli.py")
    os.remove("spec.py")


if __name__ == "__main__":
    run()
