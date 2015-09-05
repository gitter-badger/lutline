#!/usr/bin/env python
#-*- coding:utf-8 -*-


from . import python


def export(usage, lut, language="python"):
    nonenize = lambda o: "" if o == None else unicode(o)
    elementize = lambda e: ";".join(nonenize(lii) for lii in e)
    listify = lambda l: ":".join(elementize(li) for li in l) if l else ""
    lut_str = "_".join(
        ",".join([listify(emb), listify(exp), nonenize(imp)])
        for emb, exp, imp in lut)
    rst = python.TEMPLATE.replace("{{usage}}", usage)
    rst = rst.replace("{{lut}}", lut_str)
    return rst
