from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xfindIndex import _xfind_index

@_curry2
@_dispatchable([], _xfind_index)
def find_index(fn, xs):
    for idx, item in enumerate(xs):
        if fn(item):
            return idx
    return -1