import itertools

def offset_tee(iterable, offset=0):
    a, b = itertools.tee(iterable)
    try:
        for x in range(offset):
            next(b)
        return a, b
    except StopIteration:
        return a, []

def pairwise(iterable):
    return zip(*offset_tee(iterable, offset=1))


