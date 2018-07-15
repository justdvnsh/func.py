from src.funcpy.core.curry_1 import _curry1
import collections

@_curry1
def length(xs):
    return len(xs) if isinstance(xs, collections.Sequence) \
        else len(inspect.signature(xs).parameters) \
        if isinstance(xs, collections.Callable) \
        else xs.length if hasattr(xs, "length") and isinstance(xs.length, int) \
        else float("nan")