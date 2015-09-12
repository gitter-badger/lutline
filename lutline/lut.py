#!/usr/bin/env python
#-*- coding:utf-8 -*-


def generate(leafs):
    exps = u'cf'
    lut = []
    for leaf in leafs:
        l = len(leaf)
        idxs = [i for i, e in enumerate(leaf) if e[0] in exps]
        rst = (leaf[i] for i in idxs)
        rst = ''.join((e if k != 'f' else ('-' + e) for k, e in rst))
        emb = [(e if k != 'f' else ('-' + e)) for k, e in leaf]
        lut.append((l, idxs, rst, emb))
    lut.sort(key=lambda i: i[0])
    return lut
