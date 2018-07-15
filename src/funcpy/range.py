from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.isNumber import _is_number
import builtins

@_curry2
def range(from_, to):
    if not _is_number(from_) and _is_number(to):
        raise TypeError("Both arguments to range must be numbers")
    return builtins.range(from_, to)