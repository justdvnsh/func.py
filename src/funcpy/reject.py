from src.funcpy.core.curry_2 import _curry2
from src.funcpy.filter import filter
from src.funcpy.core.complement import _complement

@_curry2
def reject(pred, filterable):
    return filter(_complement(pred), filterable)