import functools 
from src.funcpy.core.xreduceBy import _xreduce_by
from src.funcpy.core.reduce import _reduce

@functools.partial(_curry_n, 4, [])
@_dispatchable([], _xreduce_by)
def reduce_by(value_fn, value_acc, key_fn, xs):
    def _fn(acc, elt):
        key = key_fn(elt)
        acc[key] = value_fn(acc.get(key, copy.copy(value_acc)), elt)
        return acc
    return _reduce(_fn, {}, xs)
