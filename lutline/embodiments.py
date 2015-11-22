#!/usr/bin/env python3


import itertools
from . import tools


def __expand(key, body):
    key = key.lower()
    #print "    expand:", key, "->", body
    if key == 'required':
        yield body
    elif key == 'optional':
        yield body
        yield None
    elif key == 'exclusive':
        for bi in body:
            #print "    bi:", bi
            yield [bi]
    elif key == 'unordered':
        n = len(body)
        for idxs in itertools.permutations(range(n), n):
            #yield [li for idx in idxs for li in body[idx]]
            yield [body[idx] for idx in idxs]
    else:
        exit("ERROR in SPEC: %s->%s" % (key, body))


def process(root):
    assert type(root) == list and len(root) == 2
    root_node = [root]
    queue = [root_node]
    leafs = []
    jdx = 0
    while queue:
        node = queue.pop(-1)
        #print(jdx, "node>", tools.lst_to_pattern(node))
        jdx += 1
        hit = next((n for n in node if type(n[1]) == list), None)
        if hit == None:
            #print("    leafed", node)
            leafs.append(node)
        else:
            idx = node.index(hit)
            start = node[:idx]
            end = node[idx + 1:]
            for n in __expand(*hit):
                new = start + (n if n != None else []) + end
                #print("    appending:", new)
                queue.append(new)
    return leafs



