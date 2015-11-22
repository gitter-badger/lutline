#!/usr/bin/env python3


import json
import itertools


def __expand(key, body):
    #print "    expand:", key, "->", body
    if key == 'req':
        yield body
    elif key == 'opt':
        yield body
        yield None
    elif key == 'exc':
        for bi in body:
            #print "    bi:", bi
            yield bi
    elif key == 'uns':
        n = len(body)
        for idxs in itertools.permutations(range(n), n):
            yield [li for idx in idxs for li in body[idx]]
    else:
        exit("ERROR in SPEC: %s->%s" % (key, body))


def process(root):
    root = json.loads(root if type(root) == unicode else json.dumps(root))
    queue = [root]
    leafs = []
    jdx = 0
    #print
    while queue:
        node = queue.pop(-1)
        #print jdx, "node>", ", ".join(("%s: (...)" % n[0]) for n in node)
        jdx += 1
        hit = next((n for n in node if type(n[1]) == list), None)
        if hit == None:
            #print "    leafed"
            leafs.append(node)
        else:
            idx = node.index(hit)
            start = node[:idx]
            end = node[idx + 1:]
            for n in __expand(*hit):
                if n == None:
                    #print "    appending:", start + end
                    queue.append(start + end)
                else:
                    #print "    appending:", start + n + end
                    queue.append(start + n + end)
    return leafs
