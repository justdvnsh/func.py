from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xfindLast import _xfind_last

@_curry2
@_dispatchable([], _xfind_last)
def find_last(fn, xs):
    for item in reversed(xs):
        if fn(item):
            return item