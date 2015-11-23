#!/usr/bin/env python3


from . import tools


def generate(leafs):
    keylib = tools.KeyLib(leafs)
    lut = []
    for leaf in leafs:
        l = len(leaf)
        idxs = [i for i, e in enumerate(leaf) if e[0] == 'explicit']
        rst = ''.join([str(leaf[i][1]) for i in idxs])
        emb = [keylib.get(*element) for element in leaf]
        lut.append((l, idxs, rst, emb))
        # Ambiguous embodiments will be appended twice ;)
    lut.sort(key=lambda i: i[0])
    return lut
