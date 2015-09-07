#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys

import embodiments
import validate
import lut
import formatize


USAGE = """usage: lutline [-l <language>] [-o <output_file>] <spec_file>
       lutline dump <spec_file>

Commands:
    dump              Prints out the pattern parsed from the spec_file.

Options and arguments:
    -l <language>     Sets the output programming language. Default is 'python'.
    -o <output_file>  Sets the name of the output file to dump the parser code.
                      Default is 'cli.py'.
    <spec_file>       Sets the input file with the specification.
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


class Node:
    def __init__(self, key, child):
        self.key = key
        self.child = child if type(child) == str else [Node(*n) for n in child]

    def __str__(self):
        if self.key == 'f':
            return "-%s" % self.child
        elif self.key == 'a':
            return "<%s>" % self.child
        elif self.key == 'c':
            return "%s" % self.child
        elif self.key == 'opt':
            return "[" + " ".join(str(c) for c in self.child) + "]"
        elif self.key == 'exc':
            return "(" + "|".join(str(c) for c in self.child) + ")"
        elif self.key == 'req':
            return "(" + " ".join(str(c) for c in self.child) + ")"
        elif self.key == 'uns':
            return "{" + " ".join(str(c) for c in self.child) + "}"

def pattern_str(spec):
    return " ".join(str(Node(*root)) for root in spec)


def main():
    args = cli()
    dump = args.get("dump")
    language = args.get("language", "python")
    output_file = args.get("output_file", "cli.py")
    spec, usage = "", ""
    with open(args["spec_file"]) as f:
        exec(f.read())
    if dump:
        print pattern_str(spec)
    else:
        embs = embodiments.process(spec)
        validate.process(embs)
        lutable = lut.generate(embs)
        rst = formatize.export(usage, lutable, language)
        with open(output_file, "w") as f:
            f.write(rst)


if __name__ == "__main__":
    main()
