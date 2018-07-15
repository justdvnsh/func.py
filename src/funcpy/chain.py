from src.funcpy.core.curry2 import _curry2
from src.funcpy.core.xchain import _xchain
from src.funcpy.core.makeFlat import _make_flat
import collections
from src.funcpy.map import map

@_curry2
@_dispatchable(["chain"], _xchain)
def chain(fn, monad):
    if isinstance(monad, collections.Callable):
        return lambda x: fn(monad(x))(x)
    return _make_flat(False)(map(fn, monad))
