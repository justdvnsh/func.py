from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.curry_3 import _curry3
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xfilter import _xfilter
import collections
from src.funcpy.core.reduce import _reduce

@_curry2
@_dispatchable(["filter"], _xfilter)
def filter(pred, filterable):
    if isinstance(filterable, collections.Mapping):
        def _fn(acc, key):
            if pred(filterable[key]):
                acc[key] = filterable[key]
            return acc
        return _reduce(_fn, {}, filterable.keys())
    return [x for x in filterable if pred(x)]


reduce = _curry3(_reduce)