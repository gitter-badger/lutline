#!/usr/bin/env python3


class Node:
    def __init__(self, key, child):
        self.key = key
        self.child = child if type(child) == str else [Node(*n) for n in child]

    def __str__(self):
        if self.key == 'explicit':
            return "%s" % self.child
        elif self.key == 'implicit':
            return "<%s>" % self.child
        elif self.key == 'optional':
            return "[" + " ".join(str(c) for c in self.child) + "]"
        elif self.key == 'exclusive':
            return "(" + "|".join(str(c) for c in self.child) + ")"
        elif self.key == 'required':
            return "(" + " ".join(str(c) for c in self.child) + ")"
        elif self.key == 'unordered':
            return "{" + " ".join(str(c) for c in self.child) + "}"


def lst_to_pattern(lst):
    return " ".join(str(Node(*root)) for root in lst)
