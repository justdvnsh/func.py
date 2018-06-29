from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xmap import _xmap
import collections
import functools
import inspect
from src.funcpy.core.curry_N import _curryN

@_curry2
@_dispatchable(["map"], _xmap)
def map(fn, functor):
    if isinstance(functor, collections.Callable):
        return _curryN(
            len(inspect.signature(functor).parameters),
            lambda *args: fn(functor(*args)))
    elif isinstance(functor, collections.Mapping):
        return functools.reduce(
            lambda acc, key: acc.update({key: fn(functor[key])}) or acc,
            functor.keys(), {})
    else:
        return [fn(x) for x in functor]