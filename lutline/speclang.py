#!/usr/bin/env python3


def split_sections(spec_str):
    # Note: This function might be improved in the future using the re module
    join = lambda ls: "\n".join(ls).strip()
    lines = spec_str.splitlines()
    __gen = (i for i, l in enumerate(lines) if l.startswith("usage:"))
    ini = next(__gen, None)
    p = join(lines if ini == None else lines[:ini])
    p = p if len(p) else None
    if ini == None:
        return p, None, None
    lines = lines[ini:]
    __gen = (i for i, l in enumerate(lines) if i != 0 and not l.startswith(" "))
    ini = next(__gen, None)
    u = join(lines if ini == None else lines[:ini])
    __u = u[6:].strip()
    u = (u if len(__u) else None) if len(u) else None
    if ini == None:
        return p, u, None
    d = join(lines[ini + 1:])
    return p, u, d if len(d) else None


def remove_comments(spec_str):
    lines = [(i + 1, l) for i, l in enumerate(spec_str.splitlines())]
    lines = [(i, l[:l.find('#') if '#' in l else None]) for i, l in lines]
    lines = [(i, l.rstrip()) for i, l in lines]
    lines = [(i, l) for i, l in lines if len(l)]
    lines = [(i, len(l) - len(l.lstrip()), l.lstrip()) for i, l in lines]
    return lines


class Node:

    def __init__(self):
        self.level = None
        self.lines = []
        self.children = []

    def grab(self, lines):
        for idx, (ln, level, line) in enumerate(lines):
            if self.level == None:
                self.level = level
            elif level <= self.level:
                return lines[idx:]
            self.lines.append((ln, level, line))
        return []

    def expand(self):
        remaining = self.lines[1:]
        while True:
            if not remaining:
                break
            node = Node()
            remaining = node.grab(remaining)
            self.children.append(node)
        return self.children

    def __str__(self):
        sep = ' ' * self.level
        stmt = self.lines[0][2]
        if stmt[-1] == ':':
            children = ',\n'.join(str(c) for c in self.children)
            return sep + "['%s', [\n%s\n" % (stmt[:-1], children) + sep + "]]"
        stmt = stmt.split()
        return sep + "[%s]" % (', '.join("'%s'" % s for s in stmt))


def parse(spec_fn=None, spec_str=None):
    __flag = ((spec_fn == None and type(spec_str) == str) or
              (spec_str == None and type(spec_fn) == str))
    assert __flag, "usage is lutline.speclang.parse(<spec_fn> | <spec_str>)"
    if spec_fn:
        with open(spec_fn, 'r') as f:
            spec_str = f.read()
    assert type(spec_str) == str
    pattern, usage, description = split_sections(spec_str)
    assert pattern != None, "pattern is missing in the CLI specification"
    lines = remove_comments(pattern)
    root = Node()
    remaining = root.grab(lines)
    assert not len(remaining)
    queue = [root]
    while queue:
        node = queue.pop(-1)
        queue += node.expand()
    return eval(str(root)), usage, description
