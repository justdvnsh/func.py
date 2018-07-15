from src.funcpy.core.curry_3 import _curry3

@_curry3
def insert_all(idx, elts, xs):
    idx = idx if len(xs) and idx >= 0 else len(xs)
    return xs[: idx] + elts + xs[idx:]
