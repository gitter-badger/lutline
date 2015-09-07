#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import subprocess


def run():
    spec = """\
spec = [
    ['opt', [
        ['f', 'f'],
        ['a', 'file_in']
    ]],
    ['a', 'file_out']
]
"""
    with open("spec.py", "w") as f:
        f.write(spec)
    print
    subprocess.call("python lutline/main.py spec.py", shell=True)
    os.remove("spec.py")
