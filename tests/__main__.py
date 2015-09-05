#!/usr/bin/env python
#-*- coding:utf-8 -*-



import pkgutil
import importlib


for _, name, _ in pkgutil.iter_modules(['tests']):
    if name != "__main__":
        importlib.import_module("." + name, "tests").run()
