#!/usr/bin/env python3


import itertools
from . import tools


def __expand(key, body):
    key = key.lower()
    if key == 'required':
        yield body
    elif key == 'optional':
        yield body
        yield None
    elif key == 'exclusive':
        for bi in body:
            yield [bi]
    elif key == 'anyset':
        n = list(range(len(body)))
        for k in n:
            for idxs in itertools.permutations(n, k + 1):
                yield [body[idx] for idx in idxs]
    else:
        exit("ERROR in SPEC: %s->%s" % (key, body))


def process(root, verbose=False):
    assert type(root) == list and len(root) == 2
    leafs = []
    jdx = 0
    queue = [(jdx, [root])]
    while queue:
        ldx, node = queue.pop(-1)
        children = []
        hit = next((n for n in node if type(n[1]) == list), None)
        if hit == None:
            leafs.append(node)
        else:
            idx = node.index(hit)
            start = node[:idx]
            end = node[idx + 1:]
            for n in __expand(*hit):
                new = start + (n if n != None else []) + end
                jdx += 1
                queue.append((jdx, new))
                children.append(jdx)
        if verbose:
            head = "#%d %s:" % (ldx, "  leaf" if hit == None else "branch")
            patt = tools.lst_to_pattern(node)
            downrefs = ", children: " + ", ".join(str(s) for s in children)
            print(head.rjust(15), patt + downrefs)
    return leafs



