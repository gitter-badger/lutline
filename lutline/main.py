#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys


USAGE = """usage: lutline [-l <language>] [-o <output_file>] <spec_file>
       lutline dump <spec_file>

Commands:
    dump              Prints out the pattern parsed from the spec_file.

Options:
    -l <language>     Sets the output programming language. Default is 'py'.
    -f <spec_file>    Sets the input file with the specification.
    -o <output_file>  Sets the name of the output file to dump the parser code.
                      Default is 'cli.py'.
"""


def cli(argv=sys.argv[1:]):
    lut = (",-l;1:-o;2:dump;3,4|,,7|,,4|,,2|a;spec_file,,|c;dump:a;spec_file,,|"
           ",,1|f;o:a;output_file:a;spec_file,,|,-o;1,2|,,2|f;l:a;language:a;sp"
           "ec_file,,|,,1|f;l:a;language:f;o:a;output_file:a;spec_file,,")
    getline = lambda l: l[:None if -1 == l.find("|") else l.find("|")]
    lst = lambda s: [e.split(";") for e in s.split(":")] if ";" in s else s
    expand = lambda s: None if s == '' else lst(s)
    emb, exs, imp = (expand(e) for e in getline(lut).split(","))
    forward = lambda l: None if -1 == l.find("|") else l[l.find("|") + 1:]
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


def main():
    args = cli()
    print args


if __name__ == "__main__":
    main()
