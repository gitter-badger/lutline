#!/usr/bin/env python
#-*- coding:utf-8 -*-



import sys
import pkgutil
import importlib
import traceback


for _, name, _ in pkgutil.iter_modules(['tests']):
    if name != "__main__":
        print "%s..." % name,
        sys.stdout.flush()
        try:
            importlib.import_module("." + name, "tests").run()
        except Exception as e:
            print
            traceback.print_exc()
            print "NOK!"
            break
        else:
            print "OK"
