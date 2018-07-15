from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xdropLast import _xdrop_last
from src.funcpy.take import take

@_curry2
@_dispatchable([], _xdrop_last)
def drop_last(n, xs):
    return take(len(xs) - n if n < len(xs) else 0, xs)