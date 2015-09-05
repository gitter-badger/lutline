#!/usr/bin/env python
#-*- coding:utf-8 -*-


def __check_uniques(embodiments):
    __s = set()
    __hashes = ("".join("".join(xi) for xi in x) for x in embodiments)
    if any(x in __s or __s.add(x) for x in __hashes):
        exit("Ambiguous CLI specification.")


def process(embodiments):
    __check_uniques(embodiments)
    # TODO: check that all pairs are not Ambiguous
