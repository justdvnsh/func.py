from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.equals import _equals

@_curry2
def ends_with(suffix, xs):
    return _equals(xs[-len(suffix):], suffix)