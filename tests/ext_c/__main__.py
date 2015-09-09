#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
import os
import pkgutil
import traceback


os.chdir(os.path.dirname(os.path.abspath(__file__)))
for _, name, _ in pkgutil.iter_modules(["."]):
    if name != "__main__":
        print "%s..." % name,
        sys.stdout.flush()
        try:
            __import__(name).run()
        except Exception as e:
            print
            traceback.print_exc()
            print "NOK!"
            break
        else:
            print "OK"
