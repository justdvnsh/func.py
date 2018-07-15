from src.funcpy.core.curry_2 import _curry2


@_curry2
def nth(offset, xs):
    try:
        return xs[offset]
    except IndexError:
        return "" if isinstance(xs, str) else None