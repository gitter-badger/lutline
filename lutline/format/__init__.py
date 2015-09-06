#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os.path


def export(usage, lut, language_ext="py"):
    nonenize = lambda o: "" if o == None else unicode(o)
    elementize = lambda e: ";".join(nonenize(lii) for lii in e)
    listify = lambda l: ":".join(elementize(li) for li in l) if l else ""
    lut_str = "|".join(
        ",".join([listify(emb), listify(exp), nonenize(imp)])
        for emb, exp, imp in lut)
    n = 67
    npartitions = int(len(lut_str) / float(n)) + 1
    lut_str = [lut_str[i * n:(i * n) + n] for i in range(npartitions)]
    lut_str = '"\n           "'.join(lut_str)
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, "template." + language_ext)
    try:
        with open(path, "r") as f:
            template = f.read()
    except IOError:
        exit("Programming language is not recognized.")
    rst = template.replace("{{usage}}", usage)
    rst = rst.replace("{{lut}}", lut_str)
    return rst
