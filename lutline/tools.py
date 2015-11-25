#!/usr/bin/env python3


class Node:

    def __init__(self, key, child):
        self.key = key.lower()
        self.child = child if type(child) == str else [Node(*n) for n in child]

    def __str__(self):
        if self.key == 'explicit':
            return "%s" % self.child
        elif self.key == 'implicit':
            return "<%s>" % self.child
        elif self.key == 'optional':
            return "[ " + " ".join(str(c) for c in self.child) + " ]"
        elif self.key == 'exclusive':
            return "( " + " | ".join(str(c) for c in self.child) + " )"
        elif self.key == 'required':
            return "( " + " ".join(str(c) for c in self.child) + " )"
        elif self.key == 'anyset':
            return "{ " + " ".join(str(c) for c in self.child) + " }"


def lst_to_pattern(lst):
    return " ".join(str(Node(*root)) for root in lst)


class KeyLib:

    def __init__(self, leafs):
        self.implicits = {}
        self.implicits.update({
                k: k for leaf in leafs for t, k in leaf
                if t == 'implicit' and k not in self.implicits})
        salt = lambda e: '_explicit' if e in self.implicits else ''
        self.explicits = {}
        self.explicits.update({
                k: (k + salt(k)) for leaf in leafs for t, k in leaf
                if t == 'explicit' and k not in self.explicits})
        self.router = {'implicit': self.implicits, 'explicit': self.explicits}

    def get(self, type, value):
        return self.router[type][value]
