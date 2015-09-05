#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys


USAGE = 'usage: {{usage}}'


def parse(argv=sys.argv[1:]):
    lut = "{{lut}}"
    getline = lambda l: l[:None if -1 == l.find("_") else l.find("_")]
    lst = lambda s: [e.split(";") for e in s.split(":")] if ";" in s else s
    expand = lambda s: None if s == '' else lst(s)
    emb, exs, imp = (expand(e) for e in getline(lut).split(","))
    forward = lambda l: None if -1 == l.find("_") else l[l.find("_") + 1:]
    for arg in argv:
        h = next((e1 for e0, e1 in exs if arg == e0), None) if exs else None
        if not (h or imp):
            sys.exit(USAGE)
        for i in range(int(h if h else imp)):
            lut = forward(lut)
        emb, exs, imp = (expand(e) for e in getline(lut).split(","))
    f = lambda a, t: t != "f" and a[0] == "-" or t == "f" and a[0] != "-"
    if not emb or any(f(a, t) for a, (t, l) in zip(argv, emb)):
        sys.exit(USAGE)
    return {l: argv[i] for i, (t, l) in enumerate(emb)}


if __name__ == "__main__":
    print parse()
