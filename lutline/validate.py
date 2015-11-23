#!/usr/bin/env python3


import itertools as it


def is_ok(lut):
    generator = zip(it.islice(lut, len(lut) - 1), it.islice(lut, 1, None))
    for (la, ia, ra, ea), (lb, ib, rb, eb) in generator:
        if la == lb and ia == ib and ra == rb and ea != eb:
            return False
    return True

