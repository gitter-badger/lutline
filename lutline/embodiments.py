#!/usr/bin/env python
#-*- coding:utf-8 -*-


import itertools


def __expand(key, body):
    if key == 'req':
        yield body
    elif key == 'opt':
        yield body
        yield None
    elif key == 'exc':
        for bi in body:
            yield bi
    elif key == 'uns':
        n = len(body)
        for idxs in itertools.permutations(range(n), n):
            yield [body[idx] for idx in idxs]
    else:
        exit("ERROR in SPEC")


def all_embodiments(root):
    __flag = lambda e: type(e) == list and type(e[1]) == list
    queue = [root]
    leafs = []
    while queue:
        node = queue.pop(-1)
        hit = next((e for e in node if __flag(e)), None)
        if hit == None:
            leafs.append(node)
        else:
            idx = node.index(hit)
            start = node[:idx]
            end = node[idx + 1:]
            for n in __expand(*hit):
                queue.append((start + n + end) if n else (start + end))
    return leafs
