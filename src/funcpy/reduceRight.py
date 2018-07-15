from src.funcpy.core.curry_3 import _curry3

@_curry3
def reduce_right(fn, acc, xs):
    return _reduce(lambda value, acc: fn(acc, value), acc, reversed(xs))