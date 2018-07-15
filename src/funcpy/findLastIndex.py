from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xfindLastIndex import _xfind_last_index

@_curry2
@_dispatchable([], _xfind_last_index)
def find_last_index(fn, xs):
    for idx, item in enumerate(reversed(xs)):
        if fn(item):
            return len(xs) - 1 - idx
    return -1