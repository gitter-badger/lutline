#!/usr/bin/env python
#-*- coding:utf-8 -*-


import subprocess


def run():
    spec = """\
spec = [
    
]
"""
    with open("spec.py", "w") as f:
        f.write(spec)
    print
    subprocess.call("python lutline/main.py spec.py", shell=True)
