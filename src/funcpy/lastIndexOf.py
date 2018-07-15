from src.funcpy.core.curry_3 import _curry3
from src.funcpy.core.checkForMethod import _check_for_method
from src.funcpy.core.equals import _equals

@_curry2
@_check_for_method("last_index_of")
def last_index_of(target, xs):
    for idx, item in enumerate(reversed(xs)):
        if _equals(item, target):
            return len(xs) - 1 - idx
    return -1