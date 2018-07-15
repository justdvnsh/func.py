from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.concat import _concat

@_curry2
def append(el, xs):
    return _concat(xs, [el])