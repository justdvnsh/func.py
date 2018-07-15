from src.funcpy.core.curry_3 import _curry3


@_curry3
def insert(idx, elt, xs):
    idx = idx if len(xs) and idx >= 0 else len(xs)
    result = xs[:]
    result.insert(idx, elt)
    return result