#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""usage: lutline [-l <language>] [-o <output_file>] <spec_file>
       lutline dump <spec_file>

Commands:
    dump              Prints out the pattern parsed from the spec_file.

Options and arguments:
    -l <language>     Sets the output programming language. Default is 'python'.
    -o <output_file>  Sets the name of the output file to dump the parser code.
                      Default is 'cli.py'.
    <spec_file>       Sets the input file with the specification.
"""


import sys

import embodiments
import validate
import lut
import templates


def parse(argv=sys.argv[1:]):
    lut = ("1,,,spec_file|2,0,dump,dump;spec_file|3,0,-o,-o;output_file;spec_fi"
           "le|3,0,-l,-l;language;spec_file|5,0;2,-l-o,-l;language;-o;output_fi"
           "le;spec_file")
    for l, idxs, rst, emb in (l.split(',') for l in lut.split('|')):
        if int(l) != len(argv):
            continue
        if rst == ''.join(argv[int(i)] for i in idxs.split(';') if len(i.strip())):
            ret = [(k, argv[i]) for i, k in enumerate(emb.split(';'))]
            if all(v[0] != '-' for k, v in ret if k[0] != '-'):
                return dict(ret)
    sys.exit(__doc__)


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


def main():
    args = parse()
    dump = args.get("dump")
    language = args.get("language", "python")
    output_file = args.get("output_file", "cli.py")
    with open(args["spec_file"]) as f:
        specfile = eval(f.read())
    spec = specfile.get("spec", "")
    usage = specfile.get("usage", "")
    if dump:
        print "Pattern:"
        print "   ", " ".join(str(Node(*root)) for root in spec)
    embs = embodiments.process(spec)
    validate.process(embs)
    lutable = lut.generate(embs)
    if dump:
        print "LUT:"
        print "   ", '"%s"' % templates.serialize(lutable)
    else:
        rst = templates.export(spec, usage, lutable, language)
        with open(output_file, "w") as f:
            f.write(rst)


if __name__ == "__main__":
    main()
