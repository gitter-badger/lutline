#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os.path


def __read_template(filename):
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, filename)
    try:
        with open(path, "r") as f:
            template = f.read()
    except IOError:
        exit("Error while loading 'lutline/templates/%s'." % filename)
    else:
        return template


def __wrap(n, s):
    npartitions = int(len(s) / float(n)) + 1
    s = [s[i * n:(i * n) + n] for i in range(npartitions)]
    sep = '"\n%s"' % ((78 - n) * ' ')
    return sep.join(s)


def serialize(lut):
    listify = lambda emb: ';'.join(''.join(e) for e in emb)
    lut_str = [",".join([str(l), ';'.join(str(i)
                         for i in idxs), rst, listify(emb)])
               for l, idxs, rst, emb in lut]
    lut_str = '|'.join(lut_str)
    return lut_str


def export(spec, usage, lut, language="python"):
    lut_str = serialize(lut)
    if language == "python":
        template = __read_template("template.py")
        lut_str = __wrap(67, lut_str)
        rst = template.replace("{{usage}}", usage)
        rst = rst.replace("{{lut}}", lut_str)
    if language == "c":
        template = __read_template("template.c")
        lut_str = __wrap(59, lut_str)
        rst = template.replace("{{usage}}", usage)
        rst = rst.replace("{{lut}}", lut_str)
        queue, args = [spec], []
        while queue:
            node = queue.pop(-1)
            for e in node:
                if len(e) == 1 or type(e[1]) == list:
                    queue.append(e[-1])
                else:
                    args.append(e)
        __s = "\n    "
        arguments = __s + __s.join("char *%s;" % l for k, l in args)
        rst = rst.replace("{{arguments}}", arguments)
        __s = "\n            "
        __t = 'if (!strcmp(buf0, "{l}"))\n                cli->{n} = argv[i];'
        labels = [(lbl if k != 'f' else ('-' + lbl)) for k, lbl in args]
        labels = [(n, l) for (k, n), l in zip(args, labels)]
        comparers = __s + __s.join(__t.format(l=l, n=n) for n, l in labels)
        rst = rst.replace("{{comparers}}", comparers)
        __s = "\n    "
        __t = 'printf("cli.{l} = \'%s\'\\n", cli.{l});'
        dumpers = __s + __s.join(__t.format(l=lbl) for k, lbl in args)
        rst = rst.replace("{{dumpers}}", dumpers)
    else:
        exit("Programming language is not recognized.")
    return rst
