from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xall import _xall
import builtins

@_curry2
@_dispatchable(["all"], _xall)
def all(fn, xs):
    return builtins.all(map(fn, xs))