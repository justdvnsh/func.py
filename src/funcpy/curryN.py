from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.curry_N import _curry_n
from src.funcpy.core.arity import _arity

@_curry2
def curry_n(length, fn):
    if length == 1:
        return _curry1(fn)
    return _arity(length, _curry_n(length, [], fn))