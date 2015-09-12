#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""{{usage}}"""


import sys


def parse(argv=sys.argv[1:]):
    lut = ("{{lut}}")
    for l, ix, r, emb in (l.split(',') for l in lut.split('|')):
        if int(l) != len(argv):
            continue
        if r == ''.join(argv[int(i)] for i in ix.split(';') if len(i.strip())):
            ret = [(k, argv[i]) for i, k in enumerate(emb.split(';'))]
            if all(v[0] != '-' for k, v in ret if k[0] != '-'):
                return dict(ret)
    sys.exit(__doc__)


if __name__ == "__main__":
    print parse()
