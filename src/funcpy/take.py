import fastnumbers
from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xtake import _xtake

@_curry2
@_dispatchable(["take"], _xtake)
def take(n, xs):
    n = fastnumbers.fast_int(n, -1)
    return xs[:] if n < 0 else xs[:n]
