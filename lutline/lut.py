#!/usr/bin/env python
#-*- coding:utf-8 -*-


class __LUT:

    def __init__(self):
        self.last_id = 0
        self.table = []
        self.append = self.table.append

    def root(self, leafs):
        return (self.new_id(), 0, leafs)

    def new_id(self):
        self.last_id += 1
        return self.last_id

    def stdout(self):
        if not self.table:
            print("<lut is empty>")
        else:
            self.table.sort(key=lambda r: r[0])
            for row in self.table:
                print(row)

    def export(self):
        self.table.sort(key=lambda r: r[0])
        return [(emb, exp, imp) for rid, emb, exp, imp in self.table]


def generate_lut(leafs):
    lut = __LUT()
    queue = [lut.root(leafs)]
    explicitize = lambda t, l: l if t == u'cmd' else ('-' + l)
    while queue:
        row_id, argv_idx, possible_leafs = queue.pop(-1)
        embodiment = next((l for l in possible_leafs if len(l) == argv_idx), None)
        items = [(explicitize(*l[argv_idx]), i)
                 for i, l in enumerate(possible_leafs)
                 if len(l) > argv_idx and l[argv_idx][0] in [u'f', u'c']]
        keys = list(set(k for k, i in items))
        explicits = []
        for key in keys:
            new_possible_leafs = [possible_leafs[i] for k, i in items if k == key]
            new_id = lut.new_id()
            explicits.append((key, new_id - row_id))
            queue.append((new_id, argv_idx + 1, new_possible_leafs))
        explicits = explicits if explicits else None
        new_possible_leafs = [l for l in possible_leafs if len(l) > argv_idx and l[argv_idx][0] == u'a']
        if new_possible_leafs:
            new_id = lut.new_id()
            implicit = new_id - row_id
            queue.append((new_id, argv_idx + 1, new_possible_leafs))
        else:
            implicit = None
        lut.append((row_id, embodiment, explicits, implicit))
    return lut.export()
