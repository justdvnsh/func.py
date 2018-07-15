from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xdropRepeatsWith import _xdrop_repeats_with
import functools

@_curry2
@_dispatchable([], _xdrop_repeats_with)
def drop_repeats_with(pred, xs):
    return functools.reduce(
        lambda acc, x: acc.append(x) or acc if not pred(x, acc[-1]) else acc,
        xs, [xs[0]]) if len(xs) else []