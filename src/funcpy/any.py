from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xany import _xany
import builtins

@_curry2
@_dispatchable(["any"], _xany)
def any(fn, xs):
    return builtins.any(map(fn, xs))