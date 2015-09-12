#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os.path


def __wrap(n, s):
    npartitions = int(len(s) / float(n)) + 1
    s = [s[i * n:(i * n) + n] for i in range(npartitions)]
    sep = '"\n%s"' % ((78 - n) * ' ')
    return sep.join(s)


def export(spec, usage, lut, language="python"):
    listify = lambda emb: ';'.join(''.join(e) for e in emb)
    lut_str = '|'.join(",".join([str(l), ';'.join(str(i) for i in idxs), rst, listify(emb)])
                       for l, idxs, rst, emb in lut)
    if language == "python":
        lut_str = __wrap(67, lut_str)
        
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, "template.py")
        try:
            with open(path, "r") as f:
                template = f.read()
        except IOError:
            exit("Error while loading lutline/templates/template.py.")
        rst = template.replace("{{usage}}", usage)
        rst = rst.replace("{{lut}}", lut_str)
    else:
        exit("Programming language is not recognized.")
    return rst
