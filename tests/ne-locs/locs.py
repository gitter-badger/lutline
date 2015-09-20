import os, sys


def read_line_count(fname):
    count = 0
    with open(fname, 'r') as f:
        for line in f.readlines():
            if len(line.strip()) > 0 and not line.rstrip().startswith('#'):
                count += 1
    return count


if __name__ == '__main__':
    exts = ['.py', '.ini', '.c', '.h']
    here = os.path.abspath(os.path.dirname(__file__))

    results = []
    listdir = os.listdir(here)
    for fn in listdir:
        if fn != "locs.py" and fn.endswith(".py"):
            key = fn.split('.')[0]
            ne_locs = read_line_count(fn)
            results.append((key, ne_locs))
    for dn in listdir:
        if dn != "locs.py" and not dn.endswith(".py"):
            ne_locs = 0
            for b, ds, fs in os.walk(dn):
                for fn in fs:
                    ne_locs += read_line_count(os.path.join(b, fn))
            results.append((dn, ne_locs))
    results.sort(key=lambda i: i[1])
    for key, ne_locs in results:
        print key, '->', ne_locs
