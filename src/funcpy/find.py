from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xfind import _xfind

@_curry2
@_dispatchable(["find"], _xfind)
def find(fn, xs):
    for item in xs:
        if fn(item):
            return item