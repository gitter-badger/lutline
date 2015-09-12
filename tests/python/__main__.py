#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
import os
import pkgutil
import traceback


cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
modules = []
for _, name, _ in pkgutil.iter_modules(["."]):
    if name != "__main__":
        modules.append(__import__(name))

os.chdir(cwd)
for module in modules:
    print "%s..." % module.__name__,
    sys.stdout.flush()
    try:
        module.run()
    except Exception as e:
        print
        traceback.print_exc()
        print "NOK!"
        break
    else:
        print "OK"
