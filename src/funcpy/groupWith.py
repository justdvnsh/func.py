from src.funcpy.core.curry_2 import _curry2

@_curry2
def group_with(fn, xs):
    res = []
    idx = 0
    while idx < len(xs):
        nextidx = idx + 1
        while nextidx < len(xs) and fn(xs[nextidx - 1], xs[nextidx]):
            nextidx += 1
        res.append(xs[idx: nextidx])
        idx = nextidx
    return res