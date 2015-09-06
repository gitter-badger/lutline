#!/usr/bin/env python
#-*- coding:utf-8 -*-



import pkgutil
import importlib


for _, name, _ in pkgutil.iter_modules(['tests']):
    if name != "__main__":
        try:
            importlib.import_module("." + name, "tests").run()
        except Exception as e:
            print name, "NOK!", e
            break
        else:
            print name, "OK"
