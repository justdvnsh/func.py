from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xdropLastWhile import _xdrop_last_while
import builtins
import itertools

@_curry2
@_dispatchable([], _xdrop_last_while)
def drop_last_while(fn, xs):
    drop = len([None for _ in itertools.takewhile(fn, builtins.reversed(xs))])
    to = len(xs) - drop
    return xs[:to]

