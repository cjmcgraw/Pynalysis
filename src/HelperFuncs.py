import itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b)
    return zip(a, b)
