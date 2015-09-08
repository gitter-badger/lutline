#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os.path


def export(spec, usage, lut, language="python"):
    nonenize = lambda o: "" if o == None else unicode(o)
    elementize = lambda e: ";".join(nonenize(lii) for lii in e)
    listify = lambda l: ":".join(elementize(li) for li in l) if l else ""
    lut_str = "|".join(
        ",".join([listify(emb), listify(exp), nonenize(imp)])
        for emb, exp, imp in lut)

    if language == "python":
        n = 67
        npartitions = int(len(lut_str) / float(n)) + 1
        lut_str = [lut_str[i * n:(i * n) + n] for i in range(npartitions)]
        lut_str = '"\n           "'.join(lut_str)
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, "template.py")
        try:
            with open(path, "r") as f:
                template = f.read()
        except IOError:
            exit("Error while loading template.py.")
        rst = template.replace("{{usage}}", usage)
        rst = rst.replace("{{lut}}", lut_str)
    elif language == "c":
        n = 58
        npartitions = int(len(lut_str) / float(n)) + 1
        lut_str = [lut_str[i * n:(i * n) + n] for i in range(npartitions)]
        lut_str = '"\n           "'.join(lut_str)
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, "template.c")
        try:
            with open(path, "r") as f:
                template = f.read()
        except IOError:
            exit("Error while loading template.c.")
        rst = template.replace("{{usage}}", usage)
        rst = rst.replace("{{lut}}", lut_str)
        elements = []
        queue = spec[:]
        while queue:
            node = queue.pop(-1)
            if type(node[1]) == list:
                [queue.append(n) for n in node[1]]
            elif node not in elements:
                elements.append(node)
        __t = ("\n            if (buf0[0] == '{t}' && !strcmp(buf1, \"{l}\"))"
               "\n                rst->{t}_{l} = argv[i];")
        inserters = "".join([__t.format(t=e[0], l=e[1]) for e in elements])
        rst = rst.replace("{{inserters}}", inserters)
        __t = ("\n    char *{t}_{l};")
        arguments = "".join([__t.format(t=e[0], l=e[1]) for e in elements])
        rst = rst.replace("{{arguments}}", arguments)
    else:
        exit("Programming language is not recognized.")
    return rst
