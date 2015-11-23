#!/usr/bin/env python3


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
    sep = '"\n"' if n >= 78 else '"\n%s"' % ((78 - n) * ' ')
    return sep.join(s)


def serialize(lut, width=None):
    listify = lambda emb: ';'.join(''.join(e) for e in emb)
    lut_str = [",".join([str(l), ';'.join(str(i)
                         for i in idxs), rst, listify(emb)])
               for l, idxs, rst, emb in lut]
    lut_str = '|'.join(lut_str)
    if width:
        return __wrap(width, lut_str)
    return lut_str


def export(lut, usage, description, language='python', width=None):
    lut_str = serialize(lut)
    if language == "python":
        template = __read_template("template.py")
        lut_str = __wrap(67 if width == None else width, lut_str)
        rst = template.replace("{{usage}}", usage)
        rst = rst.replace("{{description}}", description)
        rst = rst.replace("{{lut}}", lut_str)
    #elif language == "c":
    #    template = __read_template("template.c")
    #    usage = __wrap(55, usage)
    #    lut_str = __wrap(59, lut_str)
    #    rst = template.replace("{{usage}}", usage)
    #    rst = rst.replace("{{lut}}", lut_str)
    #
    #    args = list(set(e for l in lut for e in l[-1]))
    #    lbls = [a.replace("-", "_") for a in args]
    #
    #    __s = "\n    "
    #    arguments = __s + __s.join("char *%s;" % l for l in lbls)
    #    rst = rst.replace("{{arguments}}", arguments)
    #
    #    __s = "\n            "
    #    __t = 'if (!strcmp(buf0, "{a}"))\n                cli->{l} = argv[i];'
    #    comparers = __s.join(__t.format(l=l, a=a) for l, a in zip(lbls, args))
    #    rst = rst.replace("{{comparers}}", __s + comparers)
    #
    #    __s = "\n    "
    #    __t = 'printf("cli.{l} = \'%s\'\\n", cli.{l});'
    #    dumpers = __s + __s.join(__t.format(l=l) for l in lbls)
    #    rst = rst.replace("{{dumpers}}", dumpers)
    else:
        exit("Programming language is not recognized.")
    return rst
