def _group_by_value_fn(acc, value):
    if acc is None:
        acc = []
    acc.append(value)
    return acc

from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.checkForMethod import _check_for_method
from src.funcpy.reduceBy import reduce_by

group_by = _curry2(_check_for_method(
    "group_by", reduce_by(_group_by_value_fn, None)