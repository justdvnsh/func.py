from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xdrop import _xdrop
import builtins

@_curry2
@_dispatchable(["drop"], _xdrop)
def drop(n, xs):
    return xs[builtins.max(0, n):]
