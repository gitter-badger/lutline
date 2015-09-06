#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys


def __check_uniques(embodiments):
    __s = set()
    __hashes = ("".join("".join(xi) for xi in x) for x in embodiments)
    if any(x in __s or __s.add(x) for x in __hashes):
        sys.exit("Ambiguous CLI specification.")


def __is_ambiguous(emb0, emb1):
    uniformize = lambda k, l: (k+l) if k in [u'f', u'c'] else 'i'
    if len(emb0) == len(emb1):
        f0 = [uniformize(k, l) for k, l in emb0]
        f1 = [uniformize(k, l) for k, l in emb1]
        if f0 == f1:
            return True
    return False


def process(embodiments):
    __check_uniques(embodiments)
    for emb0 in embodiments:
        for emb1 in embodiments:
            if emb1 == emb0:
                break
            if __is_ambiguous(emb0, emb1):
                sys.exit("Ambiguous CLI specification.")
